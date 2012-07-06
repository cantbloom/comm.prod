#! /usr/bin/env python

## crontab prefs
## * * * * * /path/to/commprod_cron.py >/dev/null 2>&1  
from config import CRON
import email, imaplib, re, logging, requests, datetime, time, os, simplejson as json


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=os.path.join(ROOT_PATH, 'commprod.log'),level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

"""
Sends a post request to the endpoint of a dictionary of new messages in the form:
{sender : (content, comm_prods, date)}
or None if no new messages exist or no comm_prod was found.
"""
def fetch_prods():
    url = "http://localhost:5000/processprod"
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(CRON['EMAIL'], CRON['PASSWORD'])
        #mail.select("inbox") # connect to inbox.
        mail.select("[Gmail]/All Mail") # connect to inbox.
        result, data = mail.uid('search', None, '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))')
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
                parsed_content = parseProd(content)
                if parsed_content:
                    logging.warning("Commprod found from email %s with commprod\n '%s'" % (sender, parsed_content))
                    data = json.dumps({sender : (content, parsed_content, date)})
                    r = requests.post(url, data={'data' : data, 'key' : CRON['SECRET_KEY']})
                    time.sleep(2) # don't overload poor heroku
                    logging.info(r.text)
                    
                print "Parsed email from %s with comprods:\n %s" % (str(sender), str(parsed_content))
        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        logging.warning(str(e))

    return "Done"


"""
Returns a list of commprods if any
are found in the query, otherise 
returns None. Run query through stripOld() 
before passing in. 
"""
def parseProd(query):
    btb_regex = '((btb)|(abtb))'
    prod_regex = '((comm.prod)|(comm prod)|(commprod)|(comm.prod.)|(commprod.))'
    regex = btb_regex + '(?P<comm_prod>.+?)' + prod_regex + "+"
    pattern = re.compile(regex, re.I|re.M|re.DOTALL)
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
    forward = "---------- Forwarded message ----------"
    reply = "wrote:"
    if query != None:
        query = query.split(forward)[0]
        query = query.split(reply)[0]
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
