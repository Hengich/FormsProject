# FormsProject
Web-приложение для определения заполненных форм.

## Технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

### Настройка после клонирования репозитория.

1. Создать `.env` на основе указанного ниже примера. Указав валидные данные для подключения.

      ```ini
      SECRET_KEY=django-secret-key
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      MONGO_DB_HOST=mongodb://mongodb:27017
      MONGO_DB_PORT=27017
      MONGO_DB_NAME=mongodb
      MONGO_DB_USERNAME=root
      MONGO_DB_PASSWORD=password
      ```

2. Находясь в папке проекта `FormsProject` выполните команду `docker-compose -f docker-compose.yml up --build`.
3. По адресу http://localhost:8000 будет доступен проект
4. Необходимо выполнить миграции, для начала нужно попасть в контейнер `docker exec -t -i formsproject-backend-1 /bin/bash`
5. Затем выполните команду `python manage.py migrate`
6. Находясь в папке `/app#` выполните команду `python manage.py loaddata api/fixtures/form_templates.json`
7. Теперь вы можете проверить работоспособность проекта, выполнив команду `pytest`

### О проекте.

Сейчас в фикстуре имеется всего 2 шаблона, а именно Order Form и Contact Form следующего вида:

1. Order Form:
```
{
   "order_date": "date",
   "order_email": "email",
   "order_phone": "phone"
}
```

2. Contact Form:
```
{
   "user_email": "email",
   "user_phone": "phone"
}
```

Однако этих шаблонов хватит для проверки работоспособности проекта. Также есть возможность создать свою фикстуру, или изменить (дополнить) уже существующую.

Работу выполнил:
Есаков Даниил
