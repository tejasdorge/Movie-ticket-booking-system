from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.mail import send_mail
import binascii
import os
from cryptography.fernet import Fernet



def _generate_code():
    return binascii.hexlify(os.urandom(20)).decode('utf-8')

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
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
    def create_password_reset_code(self, user):
        code = _generate_code()
        password_reset_code = self.create(user=user, code=code)

        return password_reset_code

class AbstractBaseCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def send_email(self, prefix):
        send_mail(prefix, self.code, 'tejasjdorge@gmail.com', [self.user.email],fail_silently=False,)

    def __str__(self):
        return self.code

class PasswordResetCode(AbstractBaseCode):
    objects = PasswordResetCodeManager()

    def send_password_reset_email(self):
        prefix = 'password_reset_email'
        self.send_email(prefix)