# Быстрый деплой на PythonAnywhere

## 📋 Что нужно сделать

### 1. Регистрация (2 минуты)
- Зайди на https://www.pythonanywhere.com
- Зарегистрируйся (бесплатный аккаунт)
- Запомни свой username

### 2. Загрузка кода (3 минуты)
Открой **Bash console** и выполни:
```bash
git clone https://github.com/KingNothiing/HammerGym.git
cd HammerGym
mkvirtualenv --python=/usr/bin/python3.10 hammergym-env
pip install -r requirements.txt
```

### 3. Web App (5 минут)
**Web → Add a new web app → Manual configuration → Python 3.10**

Укажи пути (замени `yourusername` на свой):
- **Source code:** `/home/yourusername/HammerGym`
- **Working directory:** `/home/yourusername/HammerGym`
- **Virtualenv:** `/home/yourusername/.virtualenvs/hammergym-env`

### 4. WSGI файл (2 минуты)
Нажми на **WSGI configuration file** и замени содержимое:

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

### 5. Environment Variables (2 минуты)
**Web → Environment variables** добавь:

```
SECRET_KEY=uc7@h+tj2y7c(480*hu!l$me6#8e!^szhv(6$y6bc@84s(5km8
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
SECURE_SSL_REDIRECT=True
```

### 6. Static files (1 минута)
**Web → Static files** добавь:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/HammerGym/staticfiles/` |

### 7. Финальные команды (2 минуты)
В Bash console:
```bash
workon hammergym-env
cd ~/HammerGym
python manage.py collectstatic --noinput
python manage.py migrate
```

### 8. Запуск (1 минута)
Нажми зелёную кнопку **Reload** в разделе Web.

## ✅ Готово!

Сайт доступен: `https://yourusername.pythonanywhere.com`

---

## 🔄 Обновление после изменений

```bash
cd ~/HammerGym
git pull origin master
workon hammergym-env
python manage.py collectstatic --noinput
python manage.py migrate
```

Затем **Reload** в Web разделе.

---

**Время деплоя: ~15-20 минут**
