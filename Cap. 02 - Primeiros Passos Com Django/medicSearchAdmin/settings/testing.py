from .settings import *

DEBUG = True

SECRET_KEY = 'u4$8a9#a=nq^arrmwpmh*h6sr%r@l+81u)*fbze^yc-8vvq6b2'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'medicSearchAdmin',  
        'USER': 'brunos1212',  
        'PASSWORD': 'password',  
        'HOST': 'db',  
        'PORT': '5432',
    }
}