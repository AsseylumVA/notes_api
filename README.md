# Notes api


### Описание
"Notes api" – это "Python сервис,
предоставляющий REST API интерфейс для ведения заметок.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

``` git clone git@github.com:AsseylumVA/notes_api.git ``` 
``` cd notes_api/ ``` 

Создать .env файл:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
DJANGO_SUPERUSER_PASSWORD=mysecretpassword
DJANGO_SUPERUSER_EMAIL=example@example.com
DJANGO_SUPERUSER_USERNAME=admin
```

Запустить docker-compose:

```
docker compose up

```

Api будет доступно по ссылке:

```
http://localhost:8000/api/v1/notes/
```
Админ панель:
```
http://localhost:8000/admin/
```
Пользователь  `admin` будет создан сразу после запуска контейнера.

Для тестирования api создана postman коллекция в файле:
```
notes_api.postman_collection.json
```

### Автор проекта

**AsseylumVA**