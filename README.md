# Проект Email Service

### Описание
**Email Service** — это сервис для отправки имейл рассылок .

---

### Возможности:
- Отправка рассылок с использованием html макета (на выбор).
- Рассылка выбранным подписчикам из всего списка подписчиков или отфильтрованного, а так же конкретному подписчику.
- Отложенная отправка рассылок в назначенное время.
- Отслеживание открытия писем.

---

### Технологии:
- **Backend:**
  - Python 2.7
  - Django 1.9.9
  - Celery 3.1.25
  - django-celery 3.2.2
  - Rabbit MQ 3
  - SQlite
- **Frontend:**
  - HTML/CSS
  - JavaScript
  - Bootstrap 3.4
  - Jquery 1.12
- **Инфраструктура:**
  - Docker

---

### Как запустить проект:

1. Клонировать репозиторий и перейти в него:
    ```bash
    git clone git@github.com:skhfh/email_service.git
    ```
    ```bash
    cd email_service
    ```

2. Создание виртуального окружения:
    ```bash
    python2 -m pip install virtualenv
    ```
    ```bash
    python2 -m virtualenv venv27
    ```

3. Активирование виртуального окружения:
    ```bash
    source venv27/Scripts/activate
    ```

4. Установка зависимости из файла requirements.txt:
    ```bash
    pip install -r requirements.txt
    ```

5. Перейти в директорию с файлом manage.py:
    ```bash
    cd newsletterservice
    ```

6. Миграции:
    ```bash
    python manage.py migrate
    ```
    ```bash
    python manage.py migrate djcelery
    ```

7. Наполнение БД данными Подписчиков:
    ```bash
    python manage.py subscribers-in-db
    ```

8. Запуск RabbitMQ в Docker контейнере:
    ```bash
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
    ```

9. Запуск Celery:
    ```bash
    python manage.py celery -A newsletterservice worker -l info
    ```

10. Запуск Celery:
    ```bash
    python manage.py celery -A newsletterservice worker -l info
    ```

10. В другом терминале в корне проекта выполнить п.3 и п.5. Затем запуск сервиса:
    ```bash
    python manage.py runserver
    ```

---

### Подробное описание проекта и возможностей.
- На главной странице, открыв модальное окно, можно создать рассылку, заполнив поля формы:
  - Тема.
  - Содержание (вставится по тексту в шаблон).
  - Выбрать используемый шаблон.
  - Отметить получателей из всего списка подписчиков или из отфильтрованного (те, у кого день рождения в ближайший месяц).
- Кнопка отправить - письма отправятся сейчас.
- Если заполнив дату и время отложенной отправки, рассылка отправится в указанное время.
- В проекте отправка сообщений эмулируется Django. Отправленные письма можно найти в папке sent_emails.
- В html версии письма присутствует изображение для отслеживания открытия письма.
- Т.к. отправка эмулируется можно открыть указанный адрес изображения в браузере, после загрузки изображения, в БД запишется факт открытия письма.

---
### Автор 
[skhfh](https://github.com/skhfh) 
