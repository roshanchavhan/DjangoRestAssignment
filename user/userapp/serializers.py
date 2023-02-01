from rest_framework import serializers
from userapp.models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=10, min_length=6, write_only=True)

    class Meta():
        model = CustomUser
        fields = ['email', 'password','first_name', 'last_name', 'date_of_birth']

    def create(self,validated_data):
        print(validated_data)
        # return CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        return CustomUser.objects.create_user(**validated_data)



class LogInSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=10, min_length=6, write_only=True)

    class Meta():
        model = CustomUser
        fields =['email', 'password']


class LogOutSerializer(serializers.ModelSerializer):

    class Meta():
        model = CustomUser
        fields = ['email', 'password']


class DeleteSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomUser
        fields = ['email', 'password']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta():
        model = CustomUser
        fields = ['first_name', 'last_name', 'date_of_birth']


class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(
        max_length=10, min_length=6, write_only=True)
    new_password = serializers.CharField(
        max_length=10, min_length=6, write_only=True)

    class Meta():
        model = CustomUser
        fields = ['old_password', 'new_password']
