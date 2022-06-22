from pathlib import Path
import os
from decouple import config 
import dj_database_url

# Initialise environment variables
env = os.environ

SECRET_KEY = config('SECRET_KEY')


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ROOT_URLCONF = 'core.urls'

DATABASES = {'default': dj_database_url.config("DATABASE_URL")}


# CONN_MAX_AGE: To keep a connection to database open after the request is complete. This allows you to avoid creating a connection on every single request

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStore'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


