<<<<<<< HEAD
import json

from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post


def _json_body(request):
    """Parse JSON body safely."""
    try:
        return json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON body")


# -------------------------
# Users
# -------------------------

def get_users(request):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    users = list(User.objects.values("id", "username", "email", "created_at"))
    return JsonResponse(users, safe=False, status=200)


@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = _json_body(request)
        username = (data.get("username") or "").strip()
        email = (data.get("email") or "").strip()

        if not username or not email:
            return JsonResponse({"error": "username and email are required"}, status=400)

        user = User.objects.create(username=username, email=email)
        return JsonResponse({"id": user.id, "message": "User created successfully"}, status=201)

    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    except IntegrityError:
        # Handles unique constraints (duplicate username/email)
        return JsonResponse({"error": "Username or email already exists"}, status=409)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# -------------------------
# Posts
# -------------------------

def get_posts(request):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    posts = list(
        Post.objects.values("id", "content", "author_id", "created_at")
    )
    return JsonResponse(posts, safe=False, status=200)


@csrf_exempt
def create_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = _json_body(request)
        content = (data.get("content") or "").strip()
        author_id = data.get("author")

        if not content or author_id is None:
            return JsonResponse({"error": "content and author are required"}, status=400)

        try:
            author_id = int(author_id)
        except (TypeError, ValueError):
            return JsonResponse({"error": "author must be an integer user id"}, status=400)

        try:
            author = User.objects.get(id=author_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)

        post = Post.objects.create(content=content, author=author)
        return JsonResponse({"id": post.id, "message": "Post created successfully"}, status=201)

    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsPostAuthor



class UserListCreate(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return Response(
            {"id": user.id, "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED
        )


class PostListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Authentication successful!"}, status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    
class PostDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsPostAuthor]

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        return Response({"content": post.content})

class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        return Response({"message": "Authenticated!"})


>>>>>>> main
