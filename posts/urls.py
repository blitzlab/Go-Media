from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostList.as_view(), name = 'post_list'),
    path('new_post/', views.new_post, name = 'newpost'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'detail'),
    path('<slug:slug>/edit/', views.PostUpdate.as_view(), name = 'edit')
    ]
