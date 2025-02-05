from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pattern for user sign-up
    path('sign_up/', views.sign_up, name='users-sign_up'),
    
    # URL pattern for viewing and editing user profiles
    path('profile/', views.profile, name='users-profile'),
    
    # URL pattern for the login page using Django's built-in LoginView.
    # The empty string ('') means this will be the default page for this app.
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    
    # URL pattern for user logout
    path('logout/', views.logout_view, name='users-logout'),
]
