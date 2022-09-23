from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our API Views"""
    name=serializers.CharField(max_length=20)

"""model serializer: makes it easy to work with existing django models"""
class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    """the way you use a model serializer is by using a meta class to configure the serializer
     to point to specific model in our project"""

    class Meta:
        model=models.UserProfile #this sets our serializer to point to user profile model

        #specify the list of fields that you want to manage in your serializer

        fields=('id','email','name','password')
        #custom validation for pass fields so that it is write-only and nobody can retrive it
        extra_kwargs={
            'password':{
            'write_only': True,#this means that password field can be used only to create or update object but not retrieve them
            'style':{
            'input_type':'password'#this ensures that when user inputs the password it is encrypted on screen like dots or stars
            }
            }
        }
    """ovreriding the create method with create user method defined in our model class which saves the passwords as a hash value"""
    def create(self, validated_data):
        """created and return a new user"""
        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )

        return user
