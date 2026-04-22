# Быстрый чеклист деплоя

## 1. Подготовь env

Минимум для публичного демо:

```env
SECRET_KEY=<new-secret>
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com
TIME_ZONE=Europe/Chisinau
TRUST_PROXY_SSL_HEADER=True
USE_X_FORWARDED_HOST=True
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
```

Проверь:

- `.env` лежит рядом с `manage.py`
- домен совпадает с будущим адресом PythonAnywhere

## 2. Залей проект

```bash
git clone https://github.com/KingNothiing/HammerGym.git
cd HammerGym
mkvirtualenv --python=/usr/bin/python3.13 hammergym-env
pip install -r requirements.txt
```

Важно:

- текущий проект на `Django 6.0.2`
- для него нужен `Python 3.12+`
- вариант `Manual configuration -> Python 3.10` для текущего состояния проекта не подойдет без отдельного даунгрейда Django

Проверь:

```bash
workon hammergym-env
python manage.py check
python manage.py test
```

## 3. Настрой Web App

- Source code: `/home/yourusername/HammerGym`
- Working directory: `/home/yourusername/HammerGym`
- Virtualenv: `/home/yourusername/.virtualenvs/hammergym-env`
- Manual configuration: `Python 3.12` или `Python 3.13`

## 4. WSGI

```python
import os
import sys

path = '/home/yourusername/HammerGym'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hammergym_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 5. Статика и миграции

```bash
workon hammergym-env
cd ~/HammerGym
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py showmigrations
```

Static files:

| URL | Directory |
| --- | --- |
| `/static/` | `/home/yourusername/HammerGym/staticfiles/` |

## 6. Финальная проверка

- `https://yourusername.pythonanywhere.com/`
- `https://yourusername.pythonanywhere.com/health/`
- форма заявки
- карты филиалов
- стили и JS
- `https://yourusername.pythonanywhere.com/static/css/style.css`
