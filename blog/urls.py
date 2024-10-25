from . import views
from django.urls import path

urlpatterns = [
     path('', views.PostList.as_view(), name='blog'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('view_post/', views.ViewPost.as_view(), name='view_post'),
    path('update_post/<slug:slug>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
    path('show_profile/', views.EditProfileView.as_view(), name='show_profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]