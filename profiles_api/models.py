from django.db import models
#import abstract base user
from django.contrib.auth.models import AbstractBaseUser
#import abstractpermission mixin
from django.contrib.auth.models import PermissionsMixin,BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self,email,name,password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("User must have an email address")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password) ##password encryption
        user.save(using=self._db)#to save the user model

        return user

    def create_superuser(self,email,name,password):
        """create and save a new user as a super user with given details"""
        user=self.create_user(email,name,password)#self not specified bcoz it is automatically passed in any class method of same class

        user.is_superuser= True
        user.is_staff= True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""

    email=models.EmailField(max_length=225,unique=True)
    name=models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects= UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    #ForeignKey is used to link profilefeed model to UserProfile model. settings.authusermodel contains name of model
    # and ondelte parameter specifies what to do if that field is deleted from userprofile models

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )

    status_text= models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add= True)#created field for storing date time field stamp

    def __str__(self):
        return self.status_text
