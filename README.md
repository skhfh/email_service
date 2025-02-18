# email_service


установка virtualenv
python2 -m pip install virtualenv

создание ВО
python2 -m virtualenv venv27

запуск ВО
source venv27/Scripts/activate


Создание зависимостей
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py migrate djcelery

python manage.py subscribers-in-db

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

python manage.py celery -A newsletterservice worker -l info

python manage.py runserver

