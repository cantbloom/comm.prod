########## Django settings ###########

ADMIN_INFO = (
    ('Joshua Blum', 'joshblum@mit.edu'),
    ('Max Kanter', 'kanter@mit.edu'),
)

SECRET_KEY = 'mya95^-vjyf5q*8_=6xpgizqbxb*l73%9@ddj3t28*t2avsmma'
PASSWORD = 'sfbombers'


######## MYSQL #########

MYSQL = {
    'NAME' : 'joshblum+comm.prod',
    'USER' : 'joshblum',
    'PASSWORD' : PASSWORD,
    'HOST' : 'sql.mit.edu',
}


############## xvm server #############
XVM = {
    'XVM_ADDR' : 'commprod.xvm.mit.edu',
    'XVM_USER' : 'cantbloom',
    'XVM_PASSWORD' : 'sfbombers' , 
}

########### parseProd settings #########

CRON = {
    'EMAIL' : "commericalproduction@gmail.com",
    'PASSWORD' : PASSWORD,
    'SECRET_KEY': SECRET_KEY, 
}

########## SENDGRID ###############

SENDGRID = {
    'EMAIL_HOST': 'smtp.sendgrid.net',
    'EMAIL_HOST_USER': 'commprod',
    'EMAIL_HOST_PASSWORD': 'sfbombers',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
}


###### Filepicker.io ##########

FILEPICKER = {
    'API_KEY' : 'A1Os2AsKsRgK8t0gbEHcAz',
}

############# AWS ################
## setup instructions http://aws.amazon.com/articles/3998?_encoding=UTF8&jiveRedirect=1

AWS = {
    'aws_access_key_id' : 'AKIAIJ5BONOWGWS32ALQ',
    'aws_secret_access_key' : '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',
    'bucket' : 'commprod',
}