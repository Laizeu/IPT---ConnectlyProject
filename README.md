# Connectly Django API

A simple Django API for managing **Users** and **Posts** using JSON endpoints.
This project demonstrates basic CRUD operations and was tested using Postman.


## Features
- Create user (POST)
- List users (GET)
- Create post (POST)
- List posts (GET)

## Tech Stack
- Python 3.x
- Django 6.x
- SQLite

## Setup & Run
1. Clone the repo
2. Create & activate virtual environment
   ```bash
   cd connectly_project
   python3 -m venv env
   source env/bin/activate
3. Install dependencies
   ```bash
   pip install django
4. Run migrations
   ```bash
   python3 manage.py migrate
5. Start server
   ```bash
   python3 manage.py runserver

## API Endpoints
Base URL: http://127.0.0.1:PORT

## Users
GET /posts/users/
POST /posts/users/create/

```bash
{"username":"laiza","email":"laiza@example.com"}.
```

## Posts
GET /posts/posts/
POST /posts/posts/create/

```bash
{"content":"Hello this is Laiza's first post!","author":1}
```


## File Structure
```text
connectly_project/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── posts/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── env/                # virtual environment (DO NOT COMMIT)
├── db.sqlite3          # database (optional to commit)
├── manage.py
└── README.md
```

### Author
```md
Laiza Veronica Llanto
