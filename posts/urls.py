from django.urls import path
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
]
