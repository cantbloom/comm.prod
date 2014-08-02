#! /usr/bin/env python

from os import environ as env
from optparse import OptionParser
from datetime import datetime

import utils
import simplejson as json
import requests
import logging
import imaplib
import getpass
import email
import time
import re
import os


def init_parser():
    """
        Init default variables to run the parseprod with
    """
    ## defaults
    url = env['POST_URL']
    login = env['PARSE_EMAIL']
    password = env['PASSWORD']
    mailbox = 'inbox'
    search_query = '(OR (UNSEEN TO "bombers@mit.edu") (UNSEEN TO "bombers-minus-fascists@mit.edu"))'
    
    ##manual override of defaults. enter own gmail account/password and scrape prods.
    if options.debug:
        print """
            \nWelcome to commprod parser,
            please type in your gmail credentials.\n"""
        
        login = raw_input("Email: ")
        password = getpass.getpass()
        mailbox = '[Gmail]/All Mail'
        search_query = '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))'
        
        if options.mailbox:
            mailbox = options.mailbox
            print "Changed mailbox to %s" % mailbox

        if options.search_query:
            search_query = options.search_query
            print "Changed search_query to %s" % search_query

def fetch_prods(url, login, password, mailbox, search_query):
    """
        Sends a post request to the endpoint of a dictionary
        of new messages in the form:
        {sender : (content, comm_prods, date)}
        or None if no new messages exist 
        or no comm_prod was found.
    """

    print "\nStarting..."
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        ## fill in with your credentials
        mail.login(login, password)

        mail.select(mailbox)

        result, data = mail.uid('search', None, search_query)

        unread_mail = data[0].split() #list of unread uids
        for msg_id in unread_mail:
            try:
                result, data = mail.uid('fetch', 
                    msg_id, '(RFC822)')
                email_message = email.message_from_string(
                    data[0][1])
                date = email.utils.mktime_tz(
                email.utils.parsedate_tz(
                email_message['Date'])) # UTC timestamp
                date = datetime.fromtimestamp(date).isoformat()
                sender = (email.utils.parseaddr(
                    email_message['From'])[1]).lower()
                content = utils.strip_old(
                    utils.get_first_text_block(email_message))
                subject = str(email_message['Subject'])

                ##weird edge case
                if not content:
                    logging.warn(
                        "No email content found from sender %s" % str(sender))
                    continue
 
                parsed_content = parse_prod(
                    utils.clean_content(content))

                if parsed_content:
                    logging.warning(
                        """Commprod found from email 
                        %(sender)s with commprod\n 
                        '%(parsed_content)s'""" % {
                        'sender' : sender, 
                        'parsed_content' : parsed_content,
                        })
                    
                    data = json.dumps({
                        sender : (
                            utils.clean_content(content, 
                                content_type='email'),
                            parsed_content, 
                            date,
                            subject
                            )
                        })
                    
                    r = requests.post(url, 
                        data={
                        'data' : data, 
                        'key' : env['SECRET_KEY'],
                        })

                    # don't overload poor heroku
                    time.sleep(0.5) 
                    logging.info(r.text)
                
                else:
                     logging.warn("""
                     No commprods found:\n
                     Date: %(date)s \n 
                     From: %(from)s \n 
                     Subject: %(subject)s \n 
                     Content: %(content)s\n""" % {
                     'data' : date, 
                     'sender' : sender,
                     'subject' :  subject,
                     'content' :  utils.clean_content(content),
                    })
                
                print """Parsed email from %(sender)s 
                with comprods:\n %(parsed_content)s""" % {
                    'sender' : sender,
                    'parsed_content': parsed_content
                }
            
            except UnicodeDecodeError as e:
                logging.warning("""
                    UnicodeDecodeError for email %s 
                    from %s on %s""" % {
                    'content' : content, 
                    'sender' : sender,
                    'date' :  date,
                    })
                continue
        
    except imaplib.IMAP4.error as e:
        logging.warning(str(e))

    finally:
        mail.close()
        mail.logout()

    print "\nDone"

def parse_prod(query):
    """
        Returns a list of commprods if any
        are found in the query, otherise 
        returns None. Run query through strip_old() 
        before passing in. 
    """
    btb_regex = '((^)|(\s))((a btb)|(abtb)|(btb))'
    comm_regex = '(comm)(()|( )|(\.)|(\. )|( \.)|(\,)|(\, )|( \,))'
    prod_regex = '((prod)|(prodd))((\s)|(\.\s)|(\.\.\s))'
    
    commprod_regex = """((%(comm)s%(prod)s)
        |(%(comm)s\s%(prod)s))""" % {
        'comm' : comm_regex,
        'prod' :  prod_regex,
    }
    regex = '%(btb)s(?P<comm_prod>.+?)%(commprod)s+' % {
        "btb" : btb_regex,
        "commprod" : commprod_regex,
    }
    pattern = re.compile(regex, re.I|re.DOTALL)
    if pattern.search(query):
        prods = []
        for m in pattern.finditer(query):
            m = utils.strip_quotes(m.group('comm_prod'))
            prods.append(m)
        return prods
    
    return None

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    logging.basicConfig(filename=os.path.join(ROOT_PATH, 
        'commprod.log'),level=logging.DEBUG, 
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p')

    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug",
                  help="Set debug boolean", action="store_true")
    parser.add_option("-m", "--mailbox", dest="mailbox",
                  help="Use a custom mailbox -- defaults to [Gmail]/All Mail")
    parser.add_option("-s", "--search_query", dest="search_query",
                  help="""Use a custom search_query -- defaults to '(OR (TO "bombers@mit.edu") (TO "bombers-minus-fascists@mit.edu"))'""")

    (options, args) = parser.parse_args()
    url, login, password, mailbox, search_query = init_parser()
    fetch_prods(url, login, password, mailbox, search_query)

