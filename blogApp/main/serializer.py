from main.models import User , Profile,Categories,Blog
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password','date_created']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

#login serializer
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

#category serializer
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields="__all__"


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"
