# api_yamdb
### Описание
Блог, где Вы можете оценить фильмы, музыку, 
книги и многое другое. 
У нас Вы сможете подобрать произведения определенного жанра. 
Узнать, как его оценило сообщество. Оставить свою собственную рецензию, 
а также комментировать чужие отзывы. Теперь в api!
### Технологии
- Python 3.7
- Django 2.2.16
- Djangorestframework 3.12.4
- Djangorestframework-simplejwt 4.7.2
- Google
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
```
### Загрузка тестовых данных в BD
- В файле конфигурации проекта задать путь к папке с данными
```
По умолчанию
DATA_DIR = os.path.join(BASE_DIR, 'static/data/')
```
- В папке с файлом manage.py выполните команду:
```
python manage.py loadcsv
```
### Примеры запросов
- POST /api/v1/auth/token/
```json
{
  "username": "string",
  "confirmation_code": "string"
}
```
> <font color="blue">200</font>
```json
{
  "token": "string"
}
```
- GET api/v1/titles/
> <font color="green">200</font>
```json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```
- POST api/v1/titles/{title_id}/reviews/
```json
{
  "text": "string",
  "score": 1
}
```
> <font color="blue">201</font>
```json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
### Авторы
- Толпегин Денис
- Антон Пеньков 
- Митрошин Алексей