from rest_framework import serializers, validators
from django.contrib.auth import authenticate
from .models import CustomUser
# pylint: disable=W0223

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=80, required=False)
    phone_number = serializers.CharField(max_length=13, required=False)
    password = serializers.CharField()

    class Meta:
        extra_kwargs = {
            "password": {"write_only": False},
        }

    def validate(self, data):
        phone_number = data.get('phone_number')
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            username=phone_number or email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_staff', 'address',
                  'is_superuser', 'is_active')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password', 'address',
                  'is_staff', 'is_superuser', 'is_active']
        extra_kwargs = {
            "password": {"write_only": True},
            'is_staff': {"read_only": True},
            'is_superuser': {"read_only": True},
            'is_active': {"read_only": True},
            'phone_number': {"required": True, "allow_blank": False},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        CustomUser.objects.all(), f"A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        return user


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        fields = ('old_password', 'new_password')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class PasswordResetVerifiedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=128)
