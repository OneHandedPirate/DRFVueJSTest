# Тестовое задание DRF + VueJS

<details>
  <summary>ТЗ</summary>
    Реализовать API с 3мя эндпоинтами.<br>
    1.1. Принимает json с картинкой (base64) и описание картинки в виде текста.<br>
    1.2. Отдает список картинок с описанием.<br>
    1.3. Удаляет картинку из бд по ID.<br>
    Реализовать интерфейс который общается с API из пункта 1.<br>
    2.1. Форма по отправке картинки с описанием.<br>
    2.2. Список всех картинок с кнопкой удаления.<br>

</details>

<hr>

### Требования:

- docker (docker-compose)

### Установка:

- стянуть репозиторий:<br>`git clone https://github.com/OneHandedPirate/DRFVueJSTest.git`
- перейти в директорию проекта:<br>`cd DRFVueJSTest`
- создать файл `.env` со следующим набором переменных:<br>
`DJANGO_DB_NAME` - имя базы данных;<br>
`DJANGO_DB_USER` - юзернейм базы данных;<br>
`DJANGO_DB_PASSWORD` - пароль базы данных;<br>
`DJANGO_SECRET` - секретный ключ DJANGO;<br>
`DJANGO_SUPERUSER_USERNAME` - юзернейм админа бэкенда;<br>
`DJANGO_SUPERUSER_PASSWORD` - пароль админа бэкенда;<br>
`DJANGO_SUPERUSER_EMAIL` - почта админа бэкенда;<br>
  - Можно просто переименовать `.env-example` в `.env` или копировать его содержимое:<br> 
  `cat .env-example > .env`
- выполнить команду `make up`, которая запустит все необходимые контейнеры (фронт, бэк, БД). Фронт будет доступен на порту `8080`, бэк - на `8000`.
- для завершения работы выполните команду `make down`, которая остановит контейнеры, удалит образы фронта и бэка и том БД.


### Примечания:

- вместо 3 эндпоинтов я использовал вьюсет с 3 методами (GET, POST, DELETE) для лаконичности и единнобразия работы с объектами модели Image;
- валидация передаваемых на бэк картинок происходит по поиску подстроки `data:image` в начале base64-строки. Если подстроки нет - возвращает сообщение `Некорректный формат файла` с кодом `400`;
- длина описания ограничена 255 символами (на фронте и в модели Image);
- в админке бэка (`http://localhost:8000/admin`) зарегистирована модель Image, доступ в админку - по кредам, определенным в `.env`;
- если вы подняли docker-compose и остановили вручную (без команды `make up`), а затем захотели еще раз поднять - вам прежде нужно удалить том БД или команду `python manage.py createsuperuser --noinput` в 9 строке `docker-compose-dev.yaml`, иначе возникнет ошибка `Error: That username is already taken` при попытке создания суперюзера.


### Скриншоты:

- Пустая БД:<br><br>![empty.png](images%2Fempty.png)


- После добавления картинки (дата с бэка прилетает по UTC и на фронте конвертируется в местное время):<br><br>![added.png](images%2Fadded.png)


- Попытка передать не-картинку:<br><br>![incorrent.png](images%2Fincorrent.png)