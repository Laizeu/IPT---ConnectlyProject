from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path("users/", views.get_users, name="get_users"),
    path("users/create/", views.create_user, name="create_user"),
    path("posts/", views.get_posts, name="get_posts"),
    path("posts/create/", views.create_post, name="create_post"),
=======
from .views import UserListCreate, PostListCreate, CommentListCreate
from .views import UserListCreate, PostListCreate, CommentListCreate, LoginView, PostDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('token/', obtain_auth_token, name='api-token'),
>>>>>>> main
]
