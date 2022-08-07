from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api import permissions

# Create your views here.

class HelloAPIView(APIView):
    """ Test APIView"""
    serializer_class=serializers.HelloSerializer
    def get(self, request, format=None):
        """returns a simple list"""

        api_list=[
        'APIView get method demo',
        'Returns a simple list'
        ]

        return Response({'message':'success !!', 'api_list': api_list})


    def post(self, request):
        """return a hello message with our name """
        #retriever serializer . serializer_class is a standard way to retrieve the serializer class
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')#this retrieves the name field or any field that we defined in our serializer
            message=f'Hello {name}'

            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """put method demo"""
        return Response({'message':'put method'})

    def patch(self, request, pk=None):
        """put method demo"""
        return Response({'message':'patch method'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """returns a list"""
        a_viewlist=['viewset list method','viewset test methods'
        ,'user actions: (list, retrieve, create, update,partial_update)',
        'automatically maps to URLs using router']

        return Response({'message':'hello','a_viewlist':a_viewlist})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)
