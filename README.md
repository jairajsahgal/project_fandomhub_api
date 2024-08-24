<div align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src=".github/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src=".github/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</div>
<div align="center">
  <h1><strong>FandomHub - API</strong></h1>
  <a href="https://project-fandomhub-docs.pages.dev/"><strong>📚 Documentation</strong></a>
</div>
<br>
<p align="center">
An API inspired by MyAnimeList, designed for retrieving detailed information about anime and manga. It provides access to titles, genres, ratings, and user reviews, allowing users to query and explore a wide range of anime and manga content.
<p>
<p align="center">
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.11.8-blue" alt="python-version">
  </a>
  <a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/django-5.0.1-green" alt="django-version">
  </a>
  <a href="https://www.django-rest-framework.org/">
  <img src="https://img.shields.io/badge/drf-3.14.0-red" alt="django-version">
  </a>
</p>

## ⚙️ Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/project_fandomhub_api.git
```

Create a virtual environment (Optional, only if you have Python installed).

```bash
python -m venv env
```

Activate the virtual environment (Optional, only if you have Python installed).

```bash
env\Scripts\activate
```

> Notes: `(env)` will appear in your terminal input.

Install dependencies for your local environment, for testing, linter and pre-commit configs, etc. (Optional, only if you have Python installed).

```bash
pip install -r requirements/local.txt
```

Create a copy of the `.env.example` file and rename it to `.env`.

```bash
cp .env.example .env
```

**Update the values of the environment variables (Important).**

> Note: Make sure to correctly configure your variables before building the container.

## 🐳 Docker

Build your container; it will take time the first time, as Docker needs to download all dependencies and build the image.
Use the `-d` (detached mode) flag to start your containers in the background.
Use the `--build` flag if you have changes and need to rebuild.

```bash
docker compose up
docker compose up -d
docker compose up --build
```

Stop the running containers (does not remove them).

```bash
docker compose stop
```

Start previously created and stopped containers.

```bash
docker compose start
```

Show container logs in real-time.

```bash
docker compose logs -f
```

Restart a service with issues (Replace `<service_name>`).

```bash
docker compose restart <service_name>
```

Remove your container.

```bash
docker compose down
```

## 🐍 Django

Access the `web` service console that runs Django.

```bash
docker compose exec web bash
```

Inside the Django console, create the migrations.

```bash
python manage.py makemigrations
```

Run the migrations.

```bash
python manage.py migrate
```

If you need to be more specific, use:

```bash
python manage.py migrate <app_label> <migration_name>
```

List all available migrations and their status.

```bash
python manage.py showmigrations
```

> Note: Manually create the migration if Django skips an app; this happens because Django did not find the `/migrations` folder.

Create a superuser to access the entire site without restrictions.

```bash
python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access Swagger or Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## 🚨 Important Notes

Check the creation of migrations before creating them.

```bash
docker compose exec web python manage.py makemigrations users
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## 🐘 PostgreSQL

Access the PostgreSQL console.

```bash
docker compose exec db psql -U postgres -d fandomhub_db
```

List all the tables in the database.

```bash
\dt
```

Show the detailed structure of a specific table.

```bash
\d <table_name>
```

Create a backup of your database (Optional).

```bash
docker compose exec web python manage.py dumpdata > backup.json
```

Load the created backup if needed (Optional).

```bash
docker compose exec web python manage.py loaddata
```

## 🟥 Redis

```bash
docker compose exec redis redis-cli
keys *
```

## 🌍 Internationalization

Generate translation files for the languages.

```bash
django-admin makemessages -l ja --ignore=env/*
django-admin makemessages -l es --ignore=env/*
```

> Use --ignore to exclude specific directories from translation.

Compile translation files after making changes to translations.

```bash
django-admin compilemessages
```

## ⚖️ License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/project_fandomhub_api/blob/main/LICENSE).
