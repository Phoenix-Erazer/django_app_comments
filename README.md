# Django Application: Comments

This Django application enables users to engage in discussions by creating comments and responding to existing ones.

## Key Features

- **Comment Creation**: Users can easily create new comments to express their thoughts.
- **Reply Functionality**: The app allows users to reply to any existing comments, fostering interactive discussions.
- **Hierarchical Display**: Comments are displayed in a hierarchical structure, making it easy to follow conversations.

## Check it out!


### 👉 Set Up for `Windows` 

> 👉 Download the code  

```bash
$ git clone https://github.com/Phoenix-Erazer/django_app_comments.git
$ cd django_app_comments
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/comments/comment-list/`.


## ✨ Start the app in Docker

> **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/Phoenix-Erazer/django_app_comments.git
$ cd django_app_comments
```

<br />

> **Step 2** - 
To use local PostgreSQL. 
Change DATABASES in settings.py (
not necessarily an action❗❗❗)
```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
    }
}
```

<br />

> **Step 3** - Start the APP in `Docker`

```bash
$ docker build -t django_app_comments .
$ docker-compose up
```

Visit `http://127.0.0.1:8080/comments/comment-list/` in your browser. The app should be up & running.

<br />
