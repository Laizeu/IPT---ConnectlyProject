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
