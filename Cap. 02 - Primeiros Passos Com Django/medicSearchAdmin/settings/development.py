from .settings import *

DEBUG = True

SECRET_KEY = '8h24---jn#o!wda8*+4sp%up#frj5t)r014s$nfq&=2s$5px-h'

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'medicSearchAdmin',  
        'USER': 'brunos1212',  
        'PASSWORD': 'password',  
        'HOST': '127.0.0.1',  
        'PORT': '5499',
    }
}


