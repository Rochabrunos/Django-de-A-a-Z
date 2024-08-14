from .settings import *

DEBUG = True

SECRET_KEY = '%68js_p+#hy*=#lxkc-h%*2=#i49f96vyd!su=&4ve92ou+g%m'

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