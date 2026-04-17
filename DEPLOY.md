# Инструкция по деплою HammerGym на PythonAnywhere

## ✨ Что нового в проекте

**Добавленные улучшения:**
- 🎯 Sticky-навигация с эффектом при скролле
- ⬆️ Кнопка "Наверх" с плавной прокруткой
- ✨ Улучшенные hover-эффекты на карточках и кнопках
- ✅ Валидация формы в реальном времени
- 📝 Контактная форма с красивыми состояниями ошибок/успеха

---

## Шаг 1: Регистрация на PythonAnywhere
1. Перейди на https://www.pythonanywhere.com
2. Зарегистрируйся (Beginner account - бесплатно)
3. Запомни свой username (например: `yourusername`)

## Шаг 2: Загрузка кода через Git

Открой **Bash console** на PythonAnywhere и выполни:

```bash
git clone https://github.com/KingNothiing/HammerGym.git
cd HammerGym
```

## Шаг 3: Создание виртуального окружения

```bash
mkvirtualenv --python=/usr/bin/python3.10 hammergym-env
pip install -r requirements.txt
```

## Шаг 4: Настройка переменных окружения

В разделе **Web → Environment variables** добавь:

```
SECRET_KEY=uc7@h+tj2y7c(480*hu!l$me6#8e!^szhv(6$y6bc@84s(5km8
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
SECURE_SSL_REDIRECT=True
DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DJANGO_DEFAULT_FROM_EMAIL=HAMMER GYM <no-reply@hammergym.com>
HAMMERGYM_ADMIN_EMAIL=admin@hammergym.com
```

**ВАЖНО:** Замени `yourusername` на свой username!

## Шаг 5: Создание Web App

1. Перейди в **Web** → **Add a new web app**
2. Выбери **Manual configuration** → **Python 3.10**
3. Укажи пути:
   - **Source code:** `/home/yourusername/HammerGym`
   - **Working directory:** `/home/yourusername/HammerGym`
   - **Virtualenv:** `/home/yourusername/.virtualenvs/hammergym-env`

## Шаг 6: Настройка WSGI

Нажми на ссылку **WSGI configuration file** и замени содержимое на:

```python
import os
import sys

# Путь к проекту
path = '/home/yourusername/HammerGym'
if path not in sys.path:
    sys.path.append(path)

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'hammergym_project.settings'

# WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**ВАЖНО:** Замени `yourusername` на свой username!

## Шаг 7: Настройка статических файлов

В разделе **Static files** добавь:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/HammerGym/staticfiles/` |

## Шаг 8: Сборка статики и миграции

В Bash console выполни:

```bash
workon hammergym-env
cd ~/HammerGym
python manage.py collectstatic --noinput
python manage.py migrate
```

## Шаг 9: Создание суперпользователя (опционально)

```bash
python manage.py createsuperuser
```

## Шаг 10: Перезагрузка приложения

Нажми зелёную кнопку **Reload** в разделе Web.

## Готово!

Сайт доступен по адресу: `https://yourusername.pythonanywhere.com`

---

## Обновление кода после изменений

```bash
cd ~/HammerGym
git pull origin master
workon hammergym-env
python manage.py collectstatic --noinput
python manage.py migrate
```

Затем нажми **Reload** в Web разделе.
