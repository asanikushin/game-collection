# Хранилище коллекций игр
Является учебный проектом, изначально был проект https://github.com/asanikushin/shop-systems, но потом поменял тему. 

Является упрощенным клоном части фукнционала сайта [BGG](https://boardgamegeek.com/). Копируется две части: коллекции и лог (журнал) игр.

## Функционал
Пользователи могут создавать и редактировать свои коллекции игр, добавляя игры из общего списка по их `id`.
Кроме того пользователи могут выставлять играм оценки, при повторном выставлении оценки старая удаляется.

Дополнительно пользователи могут вести журнал своих игр - с кем и когда играли. Если указать других игроков, то им будет приходить уведомление при измении данных игры

## Сервисы
Графическая структура лежит [здесь](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7Vtbc6M2FP41nmkfkgGJmx99S9qdZDa7mbbZR9lWMC0gCnJi769fARIIkAl2fCHd5oHAQQjQ%2Bb5zxQM4CTa3MYpW92SJ%2FQHQlpsBnA4AAJplsX%2BpZJtLdN3hEjf2llxWCh6975gLNS5de0ucVAZSQnzqRVXhgoQhXtCKDMUxea0OeyZ%2B9a4RcnFD8LhAflP6l7ekq1zqALuU%2F4Y9dyXurFvD%2FEyAxGD%2BJskKLcmrJIKzAZzEhNB8L9hMsJ%2BunliX%2FLqbHWeLB4txSLtcEP%2B5fdpY1P0coXWYjG6Nx%2BDuCvJpXpC%2F5m88mGqDoZZux2xfHziZZDzL9nO5k23tbKtlcivb3vA3pVuxfHjJVpMfhiRk%2F8YxWYdLnD6Uxo5ITFfEJSHy7wiJmFBnwr8xpVuOBbSmhIlWNPD5Wbzx6FN6%2BbXJj75VjqYbPnd2sJUOHnDsBZjiWMhCGm%2Bf5ANppvSwnCo7EnMlFMV0lKKrfK1MduP5Ph%2FTVA9f6oSs4wVu0YmAOYpdTFvGcSKlSyzdgCv%2FFhP2pvGWDYixj6j3UgU04rxwi3EldNgOR88%2BSAJKJI00gRK21SUkAS4HOYD0bIdJDGn8VGzZgHG2P%2BH4%2B6g4K6H1Tdyl9zhzeoWzpsH6I2ELXQcEs7ZRursO%2FNGCEqaJ8QuOqccs%2Bx2aY%2F%2BBJB71SMiGzAmlJGAD%2FPTEGC3%2BcTPsTIifXsdmg8%2FZnzTHyPfc9FqaYkkGDVlT3wvxpHBHrTpKp8Ob1lUVZ2F%2BBfejpsG9ymvplCAXrSR%2FZGknUoNwgGq6mxKVRxLdHeFE2BaKkdlZbgY0YSHYdvxTcf1wHoMP6S%2Ba7mK0DLzwP09k06gy2RpemMm62cqwkkyzUtpLwumDvYK4xTp%2Byd5Afxf7YEf22b1iH2yw74GFFeFP4EhtR6vwD1ycf0O1J4UiBav505kUCI%2Bls1PJw7YnYmpKC0WjPN6s8uNUfG9l%2B%2BGkNDqS0uwVKYE6hRreSJGSHF%2BNJAwUyVORKgFJXouygASkYlgRmI3TYcDy2cKN58wgWG66V0n8QRGnsfH2jsczRPwmiglAzgI1UUPIQsGzxnj7OJwDnUudTKeHcr%2ByNKOJZI6oZ8JWQNa19e%2BaiBNXSaa8ERugO9GmPClQ%2BBXN5x69%2FyJmYw%2BXT8hB2sCR73tRksLndeVR%2FBihbLFfY1RzN0fwLLAW2UHY9Cw6ULgW51SuxXy%2FFgyVFmYB8tKbP%2BL4xWML2lEZghQrvEFuGjGMIymW49IivANvKy1%2FTkZHoDlQ%2FjOOo1FDNyoaNS%2BtUDA8q6UU%2B3tZyvfUUhc%2BShJvUStzvS9AtzoaUNFx6IkFFcZDHQwUFRLmPSdSNb7p0%2BUAsqioTFT%2BPavClq5clyROSykmywKq%2BEE8qF8wZWE5YxDRfuAtl3keiRmH0TybL0VDRLyQZktpjgfmVKn4VmY0yF20hvhdBnL3RUV67VqHmlPhvUiXOmueT%2F6Qvo00hDw%2FJwyDdWgUz3A4WqwTWfrRmhk6dvV%2Bhr5qgM7veU2no6E%2BXVKnLo8O27sbZhlYA7nTBqXYOme12STwL3NEF6tfWx2EOvM7UaZ3kPO4HkJYdSDgLQ%2BSHdWrQscLwO2O%2FsPol%2FtQRODcfdTK7ECy%2BZqUV2qDSkduJjkFIBXwbypT8Uve6aQu0EoGcllCbwXrabtyXeHWr2q%2Bwtwdxf9MEUXpvYOIabev7seqNedUJcXzuh%2FYrO%2F%2Bz%2F4W9tt9Yb%2FzIdnvnIj9tyjAWbKixewtQrf%2FkWi9BAQubQmazYUHklCX5V2NtRIh02Lre2zR4rcXbJ6v7t28EBQ9n895%2B%2BZ4K2tXV1ZXhPjWOUsxejM%2F%2F6Ara2m17ElR5jrv0io%2BSuR8TyIUdrInusqePH65Y6su2Y58ujfKlT3VmlkjxKW1BppayzLSbFERXTdpgcPljsJfUyy77R1f2JSZ4Y48sXD30IGyv7%2FWoNOenio%2BOzjcxwt4H%2B2TAUnjpkLjQnZo9UoAzqqZCbuGpPzF%2BVUlmBoT2fVv2UBtonxhGhMdq1YGVM2pI0HzgC73%2BT8Y6xpkDnuFP8M5Ev5MeGH8KYq1TKMjXUqPZqJTzpKh4e6PPGrVQjnxMqTUqpnkWVJuV5u56zeX9QrbRT4ROZQ8OxsSKxJ731ksgc7XeOpaOOTwvdKuddsyj8OpWuhndKTCiVobn%2BD9KrgyV%2FATGPq%2F2%2FN5ZN4qPvh2vz4oGlgJs9lsnE%2FQkqeKe0QdbzU%2FO4Jwn3BEqfXTGnT7LWBBTTjH89h0KCplRYP9QJtuGNWJDLN%2FQAYNIN94DJQpOEmc%2Fgyt2dIJmE2lOIX1C%2FHXAW52d0qrq3ctcChapA3Q7QQJ01lloXX7jBUO5bIqSp1Hj%2BbsQzzS%2FsHcqYzBbjheKpi7OPGPReoz5BL7Q0%2B%2FEPQUvav%2BQU%2Ff9ZnevtArHki0feoTHQw9dlj%2BLjgfXv68Gs5%2BAA%3D%3D)

Функционал разбит на два основных сервиса - сервис авторизации для работы с пользователями и основной сервис работы с данными. Во всех случаях, где требуется авторизация, пользователь указывает свой access token в хедер авторизации как `Bearer Token`

При работе со встроенными Docker образами и `docker-compose` первый будет расположен на `localhost:8082`, второй на `localhost:8081`

### Пользователи
После регистрации пользователю приходит ссылка для подтверждения регистрации, после этого появляется возможность входа в систему - получене двух токенов. 
По умолчанию все пользователи могут выполнять любые запросы на чтение (например список игр или рейтинг игры), а также выставлять свои оценки существующим играм. 

Методы API:
* /register
* /signin
* /refresh
* /validate
* /change_role

Первые 3 метода выполняются пользователем для работы. Последний метод используется админимстратором для смены ролей пользователей (например сделать админом друго пользователя)

### Коллекции игр
В данный момент есть только одна коллекция игр. Читать ее данные может любой пользователь (в том числе и без авторизации), добавлять или редактировать может только администратор.

Методы API:
* /games:
    * POST - добавление игры
    * GET -  получение всего списка игр (возможно указание количества и отступа)
* /games/<game_id>:
    * GET - получение информации об одной игре, в том числе рейтинга
    * PUT - редактирова игры
    * DELETE - удаление игры
При удалении игры вместе с ней удаляется данные про его рейтинг
    
### Рейтинг
Каждый пользователь может проголосовать зя любую созданную игру. Если игра будет удалена, то все голоса пользователей будут удалены

Методы API:
* /rating:
    * POST - добавить оценку определенной игре. Оценка и `id` игры указывается в теле запроса
    * PUT - добавить оценку определенной игре. Оценка и `id` игры указывается в теле запроса
* /rating/<game_id>:
    * GET - узнать рейтинг определенной игры. Считается как среднее по всем существующим оценкам
    * DELETE - удалить свою оценку для игры
    * PUT - позволяет изменить свою оценку
* /rating/user - получение всех своих оценок, для определения пользователя используются access token
* /rating/user/<user_id> - получение всех оценок конкретного пользователя

### Импорт данных
Есть отдельный серсив для импорта данных, он расположение на `localhost:8083`

Методы API:
* /game:
    * POST - импортировать данные из `csv`-файла.
    * GET - получить информацию по загрузке. Требуется указать ключ `batch_id` или `file_id`, которые вернули на `POST` запрос.

## Данные
Все запросы и ответы содержат данные в формате `json`.

Описание игры:
* name - обязательное поле, содержащее уникальное название игры
* category - обязательное поле, содержащее категорию игры
* min_players - необязательное поле описывает минимальное число игроков. Должено быть больше 0
* max_players - необязательное поле описывает максимальное число игроков

Если заданы min_players и max_players, то `min_players <= max_players` 

Описание оценки/голоса:
* score - обязательное поле описывает оценку - дробное число от 0 до 10 включительно
* game_id - обязательное поле, содержащее `id` игры

Описание пользователя:
* email - обязательное поле, содержащее почту пользователя, куда приходят уведомления
* password - обязательное поле, содержащее пароль для аккаунта

## Установка и запуск
### Установка
Необходимо скачать репозиторий и подтянуть необходимые подмодули:
```shell script
git clone --recursive https://github.com/asanikushin/game-collection.git
```
Если уже склонировали репозиторий, то:
```shell script
git submodule init
git submodule update
```

### Запуск
В проекте есть `docker-compose` файл для простого тестового запуска. Для локального запуска досточно выполнить:
```shell script
docker-compose up
```
Он сам скачает и соберет нужные образы. Если требуется запустить после изменения кода (например обновление репозитория), то надо указать флаг `--build` в последней команде

### Тесты
В проекте есть тесты на часть функционала. Чтобы запустить их локально требуется установленный `pytest` в питоновском окружении, сам запуск можно осуществить одной командой:
```shell script
pytest
```