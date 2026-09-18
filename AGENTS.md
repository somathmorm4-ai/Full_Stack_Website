# AGENTS.md

This file helps AI agents understand this project and work on it efficiently.

## Project Overview

A Django (6.1.1) full-stack website. The project is named `config` and contains a single app `home`.

- Backend: Django + SQLite
- Frontend: server-rendered Django templates (none exist yet; `views.py` currently returns raw `HttpResponse`)
- Python virtual environment: `venv/`

## Project Layout

```
FullStackWebsite/
├── manage.py          # Django CLI entry point
├── db.sqlite3         # SQLite database
├── config/            # Project settings (settings.py, urls.py, asgi.py, wsgi.py)
├── home/              # Main app (models.py, views.py, urls.py, admin.py, tests.py)
└── venv/              # Python virtual environment (do not commit/edit)
```

## Commands

All commands must run with the virtual environment activated:

```bash
source venv/Scripts/activate    # Windows (Git Bash)
venv\Scripts\activate           # Windows (cmd/PowerShell)

python manage.py runserver      # Start dev server at http://127.0.0.1:8000/
python manage.py migrate        # Apply DB migrations
python manage.py makemigrations # Create migrations from model changes
python manage.py createsuperuser
python manage.py test           # Run tests
```

## Code Conventions

- Follow Django 6.x idioms and the patterns already present.
- Do NOT add inline comments unless asked.
- Place new routes in `home/urls.py` and include them in `config/urls.py`.
- Use `APP_DIRS = True` templates: create templates under `home/templates/`.
- Keep business logic in views; keep `models.py` focused on data.
- When adding new apps, register them in `INSTALLED_APPS` in `config/settings.py`.

## Environment / Config Notes

- `DEBUG = True`, `ALLOWED_HOSTS = []` for development.
- Uses Django's default SQLite database at `db.sqlite3`.
- `home/urls.py` exists and defines a `home` route, but `config/urls.py` does NOT include it yet. The `home` view is not currently wired into the root URLconf.
- `home/models.py` is empty (no models yet).
- Email backend is set to console backend.

## Routes

| URL         | View            | Status                  |
|-------------|-----------------|-------------------------|
| `/admin/`   | Django admin    | Wired in `config/urls.py` |
| `/` (home)  | `home.views.home` | Defined but NOT yet wired into `config/urls.py` |

## Verification

- Run `python manage.py test` after changes touching logic.
- Run `python manage.py check` to validate project configuration.
- Verify the dev server starts with `python manage.py runserver`.