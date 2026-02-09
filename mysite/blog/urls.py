from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:pk>/', views.PostDetailVIew.as_view(), name='post'),
    path('search/', views.search, name='search'),
    path("userposts/", views.UserPostListView.as_view(), name="userposts" ),

]
