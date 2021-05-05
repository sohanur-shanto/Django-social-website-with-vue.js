from django.contrib import admin
from django.urls import path
from core.views import frontpageView, signup
from feed.views import feed, search
from django.contrib.auth import views
from feed.api import api_add_oink
from oinkerprofile.views import oinkerprofile, follow_oinker, unfollow_oinker, followers, follows

urlpatterns = [

    path('', frontpageView, name ='frontpage'),
    path('signup/', signup, name ='signup'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name ='login'),
    path('feed/', feed, name ='feed'),
    path('api/add_oink/', api_add_oink, name ='api_add_oink'),
    path('search/', search, name ='search'),
    path('u/<str:username>/', oinkerprofile, name ='oinkerprofile'),
    path('u/<str:username>/follow/', follow_oinker, name ='follow_oinker'),
    path('u/<str:username>/unfollow/', unfollow_oinker, name ='unfollow_oinker'),
    path('u/<str:username>/followers/', followers, name ='followers'),
    path('u/<str:username>/follows/', follows, name ='follows'),

]
