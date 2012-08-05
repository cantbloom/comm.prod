#! /usr/bin/env python

from os import environ as env
from optparse import OptionParser
from datetime import datetime
import email, sys, getpass, imaplib, re, logging, requests,time, os, simplejson as json


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=os.path.join(ROOT_PATH, 'commprod.log'),level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

parser = OptionParser()
parser.add_option("-d", "--debug", dest="debug",
              help="Set debug boolean", action="store_true")
parser.add_option("-m", "--mailbox", dest="mailbox",
              help="Use a custom mailbox -- defaults to [Gmail]/All Mail")
parser.add_option("-s", "--search_query", dest="search_query",
              help="""Use a custom search_query -- defaults to '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))'""")

(options, args) = parser.parse_args()


"""
Init default variables to run the parseprod with
"""
def init_parser():
    ## defaults
    url = env['POST_URL']
    login = env['PARSE_EMAIL']
    password = env['PASSWORD']
    mailbox = 'inbox'
    search_query = '(OR (UNSEEN TO "bombers@mit.edu") (UNSEEN TO "bombers-minus-fascists@mit.edu"))'
    
    ##manual override of defaults. enter own gmail account/password and scrape prods.
    if options.debug:
        print "\nWelcome to commprod parser, please type in your gmail credentials.\n"
        
        login = raw_input("Email: ")
        password = getpass.getpass() #password hidden
        mailbox = '[Gmail]/All Mail'
        search_query = '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))'
        
        if options.mailbox:
            mailbox = options.mailbox
            print "Changed mailbox to " + mailbox

        if options.search_query:
            search_query = options.search_query
            print "Changed search_query to " + search_query

    print "\nStarting..."

    fetch_prods(url, login, password, mailbox, search_query)

"""
Sends a post request to the endpoint of a dictionary of new messages in the form:
{sender : (content, comm_prods, date)}
or None if no new messages exist or no comm_prod was found.
"""
def fetch_prods(url, login, password, mailbox, search_query):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        ## fill in with your credentials
        mail.login(login, password)

        mail.select(mailbox)

        result, data = mail.uid('search', None, search_query)

        unread_mail = data[0].split() #list of unread uids
        for msg_id in unread_mail:
            try:
                result, data = mail.uid('fetch', msg_id, '(RFC822)')
                email_message = email.message_from_string(data[0][1])
                date = email.utils.mktime_tz(email.utils.parsedate_tz(email_message['Date'])) # UTC timestamp
                date = datetime.fromtimestamp(date).isoformat()
                sender = (email.utils.parseaddr(email_message['From'])[1]).lower()
                content = stripOld(get_first_text_block(email_message))
                subject = str(email_message['Subject'])

                ##weird edge case
                if content == None:
                    logging.warn("No email content found from sender %s" % str(sender))
                    continue

                ##otherwise keep going 
                parsed_content = parseProd(clean_content(content, 'commprod'))

                if parsed_content:
                    logging.warning("Commprod found from email %s with commprod\n '%s'" % (sender, parsed_content))
                    
                    data = json.dumps({
                        sender : (
                            clean_content(content, 'email'),
                            parsed_content, 
                            date,
                            subject
                            )
                        })
                    
                    r = requests.post(url, data={'data' : data, 'key' : env['SECRET_KEY']})
                    time.sleep(1) # don't overload poor heroku
                    logging.info(r.text)
                
                else:
                     logging.warn("No commprods found:\n\n Date: %s \n From: %s \n Subject: %s \n Content:\n\n%s" % (date, str(sender), subject, clean_content(content, 'commprod'))) #this is sent to commprod to help debug what the commprod parser saw.
                
                print "Parsed email from %s with comprods:\n %s" % (str(sender), str(parsed_content))
            
            except UnicodeDecodeError as e:
                logging.warning("UnicodeDecodeError for email %s from %s on %s" % (content, sender, date))
                continue
        
        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        logging.warning(str(e))

    print "\nDone"


"""
Returns a list of commprods if any
are found in the query, otherise 
returns None. Run query through stripOld() 
before passing in. 
"""
def parseProd(query):
    btb_regex = '((^)|(\s))((a btb)|(abtb)|(btb))'
    comm_regex = '(comm)(()|( )|(\.)|(\. )|( \.))'
    prod_regex = '((prod)|(prodd))((\s)|(\.\s)|(\.\.\s))'
    
    commprod_regex = '((%s%s)|(%s\s%s))'%(comm_regex, prod_regex, comm_regex, prod_regex)
    regex = btb_regex + '(?P<comm_prod>.+?)' + commprod_regex + "+"
    pattern = re.compile(regex, re.I|re.DOTALL)
    if pattern.search(query):
        prods = []
        for m in pattern.finditer(query):
            m = strip_quotes(m.group('comm_prod'))
            prods.append(m)
        return prods
    
    return None

####HELPERS#####
"""
Remove leading or trailing quotes from a string
"""
def strip_quotes(string):
    string = string.strip()
    if (string.startswith('"') or string.startswith("'")):
        string = string[1:]
    if (string.endswith('"') or string.endswith("'")):
        string = string[:-1]
    return string
    
"""
shitty hack
"""
def stripOld(query):
    strip_params = [ "---------- Forwarded message ----------",
        "-----Original message-----",
        "wrote:",
        "________________________________________",
        'Quoting',
        '\r\n>',
        '\n>',
        'From:'
        ]
    if query != None:
        for param in strip_params:
            query = query.split(param)[0]
        query+="\n" ## if there is not newline at the end, add it to pick up the commprod
        return query

def clean_content(query, type):
    if type == "email":
        query = query.replace('=\r\n', '\n')
    elif type == "commprod":
        query = query.replace('=\r\n', '')
    query = query.replace('=92', '\'')
    query = query.replace('=93', '"')
    query = query.replace('=94', '"')
    query = query.replace('=20', '')
    return query
                             
"""
Helper to read message content
"""
def get_first_text_block(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload()

#run script
init_parser()
