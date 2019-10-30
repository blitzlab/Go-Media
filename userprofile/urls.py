from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('<username>/profile/', views.ProfileDetail.as_view(), name = 'profile'),
    path('<username>/edit/', views.ProfileUpdate.as_view(), name = 'edit')
    ]
