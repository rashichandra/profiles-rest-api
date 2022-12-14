from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#we do not need to specify basename for UserProfileViewSet bcoz we already have the query object in our UserProfileViewSet classs
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns=[
    #as_view is the standard method that is called to convert api view class to be rendered by our urls
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
