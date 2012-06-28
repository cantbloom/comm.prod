#!/usr/bin/env python

##cron tab prefs
#* * * * * /path/to/commprod_cron.py
from config import EMAIL, PASSWORD
import email
import imaplib
import re
import logging
import requests
import simplejson as json
import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=os.path.join(ROOT_PATH, 'logs/commprod.log'),,level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

"""
Gets new comm prods and posts to endpoint if any new ones
are present. Logs endpoint response
"""
def post_prods():
    prods = fetch_mail()
    url = "http://comm-prod.herokuapp.com/processprod/"
    if prods:
        payload = json.dumps(prods)
        r = requests.post(url, data=payload)
        logging.info(r.text)

"""
Returns an array of dictionarys of new messages [{sender : (content, comm_prods)}]
or None if no new messages exist or no comm_prod was found.
"""
def fetch_mail():

    messages = []
    valid_senders = {'bombers@mit.edu': 0, 'bombers-minus-facists@mit.edu': 0}
    dev_send = {'joshblum@mit.edu': 0, 'kanter@mit.edu' : 0}
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(EMAIL,PASSWORD)
        mail.select("inbox") # connect to inbox.

        result, data = mail.uid('search', None, "UNSEEN") #get unread messages
        unread_mail = data[0].split() #list of unread uids

        for msg_id in unread_mail:
            result, data = mail.uid('fetch', msg_id, '(RFC822)')
            email_message = email.message_from_string(data[0][1])
            recipient = email.utils.parseaddr(email_message['To'])[1]
            sender = email.utils.parseaddr(email_message['From'])[1].split('@')[0]
            content = get_first_text_block(email_message)
            parsed_content = parseProd(content)
            if parsed_content:
                logger.warning("Commprod found from email %s with commprod '%s'" % (sender, parsed_content))
                if recipient in valid_senders or sender in dev_send:
                    messages.append({sender : (content, parsed_content)})
            else:
                logging.info("No commprod found from email %s with content %s" % (sender, content))

        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        logging.warning("IMAP error({0}): {1}".format(e.errno, e.strerror))

    return messages

"""
Returns a list of commprods if any
are found in the query, otherise 
returns None
"""
def parseProd(query):
    btb_regex = '((a btb)|(btb)|(abtb))'
    prod_regex = '((comm.prod)$|(comm prod)$|(commprod)$)'
    regex = btb_regex + '(?P<comm_prod>.+?)' + prod_regex + "+"
    pattern = re.compile(regex, re.I|re.M)
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
