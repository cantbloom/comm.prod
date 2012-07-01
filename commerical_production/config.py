ADMIN_INFO = (
    ('Joshua Blum', 'joshblum@mit.edu'),
    ('Max Kanter', 'kanter@mit.edu'),
)


##DATABASE INFO
NAME = 'joshblum+comm.prod'
USER = 'joshblum'
PASSWORD = 'sfbombers'
HOST = 'sql.mit.edu'

SECRET_KEY = 'mya95^-vjyf5q*8_=6xpgizqbxb*l73%9@ddj3t28*t2avsmma'

EMAIL = "commericalproduction@gmail.com"



############## xvm server #############
XVM = {
    'XVM_ADDR' : 'commprod.xvm.mit.edu',
    'XVM_USER' : 'cantbloom',
    'XVM_PASSWORD' : 'sfbombers'  
}



########## SENDGRID ###############

SENDGRID = {
    'EMAIL_HOST': 'smtp.sendgrid.net',
    'EMAIL_HOST_USER': 'commprod',
    'EMAIL_HOST_PASSWORD': 'sfbombers',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True
}