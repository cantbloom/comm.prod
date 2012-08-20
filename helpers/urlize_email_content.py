from commProd.models import CommProd
"""
Takes the email content from a given commprod 
and returns the content with urls inserted for the 
permalink of each commprod found.
"""

def urlize_email_content(email_content, commprods):
    for commprod in commprods:
        url  = '<a href=/commprod/%s/%s>%s</a>' % (commprod.user_profile.user.username, commprod.id, commprod.original_content)
        email_content = email_content.replace(commprod.original_content, url)
    return email_content
