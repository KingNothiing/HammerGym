# Публичный демо-деплой HammerGym

Этот сценарий рассчитан на быстрый и понятный выклад сайта наружу для показа заказчику. Базовая рекомендация для текущего состояния проекта: PythonAnywhere или другой хостинг, где можно вручную настроить WSGI и раздачу `/static/`.

## Что подготовлено в проекте

- production-friendly env-переменные
- `STATIC_ROOT` для `collectstatic`
- security-настройки Django для `DEBUG=False`
- `CSRF_TRUSTED_ORIGINS` и proxy-заголовки
- health-check endpoint: `/health/`

## 1. Подготовь продакшен `.env`

Возьми за основу `.env.production` и подставь реальные значения:

```env
SECRET_KEY=<сгенерированный-секрет>
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com
TIME_ZONE=Europe/Chisinau
TRUST_PROXY_SSL_HEADER=True
USE_X_FORWARDED_HOST=True
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DJANGO_DEFAULT_FROM_EMAIL=HAMMER GYM <no-reply@hammergym.com>
HAMMERGYM_ADMIN_EMAIL=admin@hammergym.com
```

`TRUST_PROXY_SSL_HEADER=True` подходит для стандартного деплоя за доверенным reverse proxy. Для нетипичной инфраструктуры это нужно проверить отдельно.

Что проверить после шага:

- файл `.env` лежит в корне проекта рядом с `manage.py`
- `DEBUG=False`
- `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS` совпадают с будущим адресом на PythonAnywhere
- в `SECRET_KEY` длинное случайное значение

## 2. Загрузи код

На сервере:

```bash
git clone https://github.com/KingNothiing/HammerGym.git
cd HammerGym
```

Если деплой идет без Git, загрузи архив проекта без `.env`, `db.sqlite3`, `staticfiles/` и `__pycache__/`.

Что проверить после шага:

- в каталоге проекта есть `manage.py`
- есть папки `hammergym_project/`, `gym/`, `templates/`, `static/`

## 3. Проверь совместимость Python и Django

Сейчас проект использует `Django 6.0.2`, а эта версия официально поддерживает только `Python 3.12+`. Поэтому сценарий с `Python 3.10` для текущего состояния проекта не подходит.

Без изменения кода есть безопасный путь:

- на PythonAnywhere выбрать system image, где доступен `Python 3.12` или `Python 3.13`
- создать web app и virtualenv именно на этой версии Python

Если по какой-то причине нужен строго `Python 3.10`, это уже отдельная задача с согласованием: потребуется даунгрейд Django до совместимой ветки.

Что проверить после шага:

- в аккаунте PythonAnywhere доступен `Python 3.12` или `Python 3.13`
- не выбран `Python 3.10` для текущего `requirements.txt`

## 4. Создай виртуальное окружение

```bash
mkvirtualenv --python=/usr/bin/python3.13 hammergym-env
pip install -r requirements.txt
```

Что проверить после шага:

```bash
workon hammergym-env
python --version
python manage.py check
python manage.py test
```

Ожидаемо:

- активируется `hammergym-env`
- Python версии 3.12.x или 3.13.x
- `check` и `test` проходят без ошибок

## 5. Настрой Web App

Для PythonAnywhere:

1. `Web -> Add a new web app`
2. `Manual configuration -> Python 3.12` или `Python 3.13`
3. Укажи пути:
   - Source code: `/home/yourusername/HammerGym`
   - Working directory: `/home/yourusername/HammerGym`
   - Virtualenv: `/home/yourusername/.virtualenvs/hammergym-env`

WSGI-конфиг должен указывать на проект:

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

Что проверить после шага:

- в WSGI указан путь до папки, где лежит `manage.py`
- `DJANGO_SETTINGS_MODULE='hammergym_project.settings'`
- выбран именно `Manual configuration`, а не Django quickstart

## 6. Собери статику и применяй миграции

```bash
workon hammergym-env
cd ~/HammerGym
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py showmigrations
```

После этого проверь health endpoint:

```bash
python manage.py check
```

А снаружи приложение должно отвечать на:

```text
https://yourusername.pythonanywhere.com/health/
```

Что проверить после шага:

- `collectstatic` завершается без traceback
- у `gym` и стандартных django apps миграции отмечены как `[X]`
- `https://yourusername.pythonanywhere.com/health/` возвращает JSON со статусом `ok`

## 7. Настрой раздачу статики

В PythonAnywhere `Web -> Static files`:

| URL | Directory |
| --- | --- |
| `/static/` | `/home/yourusername/HammerGym/staticfiles/` |

Что проверить после шага:

- mapping ровно `/static/`
- директория совпадает с `STATIC_ROOT`
- после reload открывается, например, `/static/css/style.css`

## 8. Перезапусти приложение

Нажми `Reload` в разделе `Web`.

Если reload падает:

- открой `error log` и `server log` на вкладке `Web`
- сначала проверь WSGI-файл и путь к virtualenv
- затем проверь `.env`, `ALLOWED_HOSTS` и наличие всех зависимостей

## 9. Финальная проверка перед показом заказчику

- открывается главная страница
- работают якоря и мобильное меню
- грузятся стили и favicon
- работает форма заявки
- открываются карты филиалов
- отвечает `/health/`
- в `admin/` открывается страница логина Django

## Регистрация на PythonAnywhere

1. Открой [pythonanywhere.com](https://www.pythonanywhere.com/).
2. Зарегистрируй аккаунт.
3. После входа проверь, какой у тебя домен:
   - обычно `yourusername.pythonanywhere.com`
   - для EU-аккаунтов возможен формат `yourusername.eu.pythonanywhere.com`
4. Сразу создай `Bash console` и открой вкладку `Web`.

Что проверить после регистрации:

- можешь открыть `Consoles -> Bash`
- можешь открыть `Web -> Add a new web app`
- понимаешь точный домен, который нужно вписать в `.env`

## Важный выбор для Environment Variables

Для этого проекта безопаснее и проще использовать `.env` в папке проекта, потому что приложение уже построено вокруг `python-decouple`. Это снижает шанс рассинхронизации между переменными в консоли и в WSGI.

Если захочешь, я могу следующим сообщением дать тебе уже готовый блок значений под твой конкретный username на PythonAnywhere.

## Что еще нужно перед реальным запуском

- заменить временный номер `111`
- подставить реальные фото залов
- подставить реальные профили тренеров
- подключить боевой email backend вместо console backend
- при росте проекта вынести данные в админку и перейти на PostgreSQL
