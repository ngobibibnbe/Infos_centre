from django.contrib.auth.models import User , Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url','id', 'username', 'password','last_login','first_name'
        ,'last_name','email','is_staff','is_active','date_joined']

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['url','id', 'name']