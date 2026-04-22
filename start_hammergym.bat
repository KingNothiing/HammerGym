@echo off
cd /d "%~dp0"
start "" http://127.0.0.1:8000/
C:\Users\Admin\AppData\Local\Python\bin\python.exe manage.py runserver
