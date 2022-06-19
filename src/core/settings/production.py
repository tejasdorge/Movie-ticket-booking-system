from pathlib import Path
import os
# from decouple import config # To Retrieve the configuration parameters (from heroku)
import django_heroku

# SECRET_KEY = config('SECRET_KEY')


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'dbohsl4h8lkdu4',

        'USER': 'nxzfmbtpztxfmi',

        'PASSWORD': '9af1318fe9986e9a17cf2c1269b2f7289065c7ba7f1d58bbb55218b4df8f8242',

        'HOST': 'ec2-54-157-16-196.compute-1.amazonaws.com',

        'PORT': '5432',

    }

}

# AWS SETTINGS

# AWS_ACCESS_KEY_ID = 'AKIASS227E3VTXHNGYV2'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'django-demo123'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_DEFAULT_ACL = 'public-read'
# AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_DEFAULT_ACL = 'public-read'

# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# AWS_LOCATION = 'static'

# AWS_QUERYSTRING_AUTH = False

# AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


