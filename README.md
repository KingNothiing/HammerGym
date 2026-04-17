# HAMMER GYM — Сайт тренажёрного зала

Презентационный сайт спортзала HAMMER GYM в Тирасполе (Приднестровье).

## О проекте

Информационный сайт с двумя филиалами:
- **Тирасполь, ул. Ларионова**
- **Оскар на Балке**

### Функционал
- Главная страница с презентацией зала
- Прайс-листы по филиалам
- Карточки тренеров
- Галерея
- Контактная информация

## Стек технологий

- **Backend:** Django 6.0+
- **База данных:** SQLite (для продакшена рекомендуется PostgreSQL)
- **Frontend:** HTML + CSS + vanilla JavaScript
- **Шрифты:** Google Fonts (Cinzel + Sora)

## Локальная разработка

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Настройка окружения
Скопируй `.env.example` в `.env`:
```bash
cp .env.example .env
```

В `.env` укажи:
- `SECRET_KEY` — сгенерируй новый: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- `DEBUG=True` (для разработки)
- `ALLOWED_HOSTS=localhost,127.0.0.1`

### 3. Применение миграций
```bash
python manage.py migrate
```

### 4. Запуск сервера
```bash
python manage.py runserver
```

Открой: http://127.0.0.1:8000

## Деплой на PythonAnywhere (бесплатно)

### 1. Регистрация
- Зайди на https://www.pythonanywhere.com
- Зарегистрируйся (Beginner аккаунт — бесплатно)

### 2. Загрузка кода
**Вариант A — через Git:**
```bash
# На PythonAnywhere Bash console:
git clone <твой-repo>
cd HammerGym
```

**Вариант B — через ZIP:**
- Заархивируй проект (без `.env`, `db.sqlite3`, `__pycache__`)
- Загрузи через Files tab на PythonAnywhere

### 3. Настройка на PythonAnywhere

#### 3.1. Virtual environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 hammergym-env
pip install -r requirements.txt
```

#### 3.2. Environment variables
В разделе **Web → Environment variables** добавь:
```
SECRET_KEY=<твой-секретный-ключ>
DEBUG=False
ALLOWED_HOSTS=<твой-username>.pythonanywhere.com
DJANGO_EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
DJANGO_DEFAULT_FROM_EMAIL=HAMMER GYM <no-reply@hammergym.com>
HAMMERGYM_ADMIN_EMAIL=admin@hammergym.com
```

#### 3.3. Web App настройка
1. Перейди в **Web** → **Add a new web app**
2. Выбери **Manual configuration** → **Python 3.10**
3. Укажи пути:
   - **Source code:** `/home/<твой-username>/HammerGym`
   - **Working directory:** `/home/<твой-username>/HammerGym`
   - **Virtualenv:** `/home/<твой-username>/.virtualenvs/hammergym-env`

4. В **WSGI configuration file** (ссылка рядом с путём):
   Найди строки:
   ```python
   # path = '/home/<твой-username>/myproject'
   ```
   Замени на:
   ```python
   path = '/home/<твой-username>/HammerGym'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'hammergym_project.settings'
   ```

5. В **Static files**:
   | URL | Directory |
   |---|---|
   | `/static/` | `/home/<твой-username>/HammerGym/staticfiles/` |
   | `/media/` | `/home/<твой-username>/HammerGym/media/` |

### 4. Collect static files
```bash
workon hammergym-env
cd ~/HammerGym
python manage.py collectstatic --noinput
```

### 5. Миграции
```bash
python manage.py migrate
```

### 6. Reload web app
Нажми зелёную кнопку **Reload** в разделе Web.

Готово! Сайт доступен по адресу: `https://<твой-username>.pythonanywhere.com`

## Деплой на Render (альтернатива)

1. Зайди на https://render.com
2. Подключи GitHub репозиторий
3. Создай **Web Service**
4. Настройки:
   - **Build command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start command:** `gunicorn hammergym_project.wsgi:application`
5. Добавь **Environment Variables**:
   ```
   SECRET_KEY=<сгенерированный-ключ>
   DEBUG=False
   ALLOWED_HOSTS=*
   ```

## Безопасность (ВАЖНО!)

Перед деплоем **ОБЯЗАТЕЛЬНО**:
1. ✅ `DEBUG=False` в `.env`
2. ✅ Сгенерируй новый `SECRET_KEY`
3. ✅ Укажи правильные `ALLOWED_HOSTS`
4. ✅ Не коммить `.env` в Git (он в `.gitignore`)

## Структура проекта

```
HammerGym/
├── hammergym_project/      # Django настройки
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── gym/                    # Django приложение
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
├── templates/              # HTML шаблоны
├── static/                 # Статические файлы (CSS, JS, images)
├── .env                    # Локальные настройки (НЕ коммить!)
├── .env.example            # Пример настроек
├── .env.production         # Шаблон для продакшена
├── requirements.txt        # Зависимости
├── Procfile                # Для деплоя
└── manage.py
```

## Лицензия

Проект создан для демонстрации клиенту. Все права защищены.
