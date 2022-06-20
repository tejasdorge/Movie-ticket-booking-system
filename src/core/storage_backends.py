from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    location = 'media'
    file_overwrite = False


# S3Boto3Storage to add a few custom parameters, in order to be able to store the user uploaded files,
# that is, the media assets in a different location and also to tell S3 to not override files with the same name