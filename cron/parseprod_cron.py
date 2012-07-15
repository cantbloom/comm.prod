#! /usr/bin/env python

## crontab prefs
## * * * * * source /home/cantbloom/commprod/venv/bin/activate >/dev/null 2>&1; python /home/cantbloom/commprod/cron/parseprod_cron.py >/dev/null 2>&1
from os import environ as env
import email, imaplib, re, logging, requests, datetime, time, os, simplejson as json


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=os.path.join(ROOT_PATH, 'commprod.log'),level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

"""
Sends a post request to the endpoint of a dictionary of new messages in the form:
{sender : (content, comm_prods, date)}
or None if no new messages exist or no comm_prod was found.
"""
def fetch_prods():
    url = "http://commprod.herokuapp.com/commprod/processprod"
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        ## fill in with your credentails
        #mail.login(env['PARSE_EMAIL'], env['PASSWORD'])
        
        mail.login('jblum18@gmail.com', 'LPK9755xml?')
        #mail.select('inbox')
        mail.select("[Gmail]/All Mail")

        result, data = mail.uid('search', None, '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))')
        #result, data = mail.uid('search', None, '(OR (UNSEEN TO "bombers@mit.edu") (UNSEEN TO "bombers-minus-fascists@mit.edu"))')
        unread_mail = data[0].split() #list of unread uids
        for msg_id in unread_mail:
            result, data = mail.uid('fetch', msg_id, '(RFC822)')

            email_message = email.message_from_string(data[0][1])
            date = time.mktime(email.utils.parsedate(email_message['Date'])) # in milliseconds
            date = datetime.datetime.fromtimestamp(date).isoformat()
            sender = (email.utils.parseaddr(email_message['From'])[1]).lower()
            content = stripOld(get_first_text_block(email_message))
            if content == None:
                logging.warn("No content found from sender %s" % str(sender))
            else:
                parsed_content = parseProd(clean_content(content, 'commprod'))
                
                if parsed_content:
                    logging.warning("Commprod found from email %s with commprod\n '%s'" % (sender, parsed_content))
                    
                    data = json.dumps({
                        sender : (
                            clean_content(content, 'email'),
                            parsed_content, 
                            date
                            )
                        })
                    
                    r = requests.post(url, data={'data' : data, 'key' : env['SECRET_KEY']})
                    time.sleep(1) # don't overload poor heroku
                    logging.info(r.text)
                print "Parsed email from %s with comprods:\n %s" % (str(sender), str(parsed_content))
        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        logging.warning(str(e))

    print "Done"


"""
Returns a list of commprods if any
are found in the query, otherise 
returns None. Run query through stripOld() 
before passing in. 
"""
def parseProd(query):
    btb_regex = '((^a btb)|(^abtb)|(\sa btb)|(\sabtb))'
    prod_regex = '((comm\.prod\s)|(comm prod\s)|(commprod\s)|(comm\.prod\s)|(commprod\.\s))'
    regex = btb_regex + '(?P<comm_prod>.+?)' + prod_regex + "+"
    pattern = re.compile(regex, re.I|re.DOTALL)
    match = pattern.search(query)
    prods = []
    if match:
        for m in pattern.finditer(query):
            m = strip_quotes(m.group('comm_prod'))
            prods.append(m)
        return prods

    return None

####HELPERS#####

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
        ]
    if query != None:
        for param in strip_params:
            query = query.split(param)[0]
        return query

def clean_content(query, type):
    if type == "email":
        query = query.replace('=\r\n', '\n')
    elif type == "commprod":
        query = query.replace('=\r\n', '')
    query = query.replace('=92', '\'')
    query = query.replace('=93', '"')
    query = query.replace('=94', '"')
    return query
                             
"""
Helper to read message content
"""
def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

fetch_prods()
