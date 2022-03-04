# YaMDB API
Учебный групповой проект "API сервиса YaMDB".

## Как запустить проект

В командной строке клонируйте проект в нужную папку и перейдите в него:
```
git clone https://github.com/NVTaranets/api_yamdb
```
```
cd api_yamdb
```
Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
Установите зависимости:
```
pip install -r requirements.txt
```
Перейдите в папку api_yamdb:
```
cd api_yamdb
```
Создайте и выполните миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Запустите проект:
```
python manage.py runserver
```
## Документация API YaMDB
После запуска проекта вам будет доступна документация проекта по адресу http://127.0.0.1:8000/redoc/, где описано, как работает проект, и представлены примеры доступных запросов.
