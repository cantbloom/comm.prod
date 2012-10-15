from commProd.models import CommProd
from helpers.urlize_tags import urlize_text

def urlize_email_content(email_content, commprods):
    """
    Takes the email content from a given commprod 
    and returns the content with urls inserted for the 
    permalink of each commprod found.
    """
    email_content = urlize_text(email_content)
    for commprod in commprods:
        url  = '<a href=/commprod/%s/%s>%s</a>' % (commprod.user_profile.user.username, commprod.id, commprod.content)

        content = commprod.content
        if commprod.media:
            content = commprod.media_content
        content = content.strip()

        email_content = email_content.replace(content, url)
    return email_content
