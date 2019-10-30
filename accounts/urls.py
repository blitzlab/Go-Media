from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'accounts'

urlpatterns = [
    path('account/login/', auth_view.LoginView.as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('account/logout/', auth_view.LogoutView.as_view(), name = 'logout'),
    path('account/signup/', views.signup, name = 'signup'),
    ]
