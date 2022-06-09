from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
import binascii
import os
from cryptography.fernet import Fernet
key = b'IqRdzA3BdkyA83m7zU3eijQfwgHDxK2oh_ID4qul61Y='
f = Fernet(key)

def _generate_code():
    return binascii.hexlify(os.urandom(20)).decode('utf-8')


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password, **extra_fields):
        if not email:
            raise ValueError("email is required")
        if not phone_number:
            raise ValueError("phone_number is required")
        email = self.normalize_email(email)
        new_user = self.model(email=email, phone_number=phone_number,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email,  phone_number, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=80,null=True,blank=True,unique=True)
    phone_number = PhoneNumberField(null=True,blank=True,unique=True)
    address = models.CharField(max_length=100,null=True,blank=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email','phone_number']
    def __str__(self):
        return self.username

class PasswordResetCodeManager(models.Manager):
    def send_mail(self, user):
        prefix = 'password_reset_email'
        code = _generate_code()
        username = user.username
        useremail = user.email
        context = ",".join([username,useremail,code])
        byte_context=bytes(context, 'utf-8')
        token = f.encrypt(byte_context)
        token = token.decode()
        print(token)
        # send_mail(prefix , token, 'tejasjdorge@gmail.com', [user.email], fail_silently=False)
        return None

class PasswordResetCode(models.Model):
    objects = PasswordResetCodeManager()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


    