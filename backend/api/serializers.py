from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers takes a python object and converts into JSON data and vice versa for communication 
# between the API and the front end

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}} # password is write only and required, it can't be read
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user