# Хранилище коллекций игр
Является учебный проектом, изначально был проект https://github.com/asanikushin/shop-systems, но потом поменял тему. 

Является упрощенным клоном части фукнционала сайта [BGG](https://boardgamegeek.com/). Копируется две части: коллекции и лог (журнал) игр.

## Функционал
Пользователи могут создавать и редактировать свои коллекции игр, добавляя игры из общего списка по их `id`.
Кроме того пользователи могут выставлять играм оценки, при повторном выставлении оценки старая удаляется.

Дополнительно пользователи могут вести журнал своих игр - с кем и когда играли. Если указать других игроков, то им будет приходить уведомление при измении данных игры

## Сервисы
Функционал разбит на два основных сервиса - сервис авторизации для работы с пользователями и основной сервис работы с данными. Во всех случаях, где требуется авторизация, пользователь указывает свой access token в хедер авторизации как `Bearer Token`

При работе со встроенными Docker образами и `docker-compose` первый будет расположен на `localhost:8082`, второй на `localhost:8081`

### Пользователи
После регистрации пользователю приходит ссылка для подтверждения регистрации, после этого появляется возможность входа в систему - получене двух токенов. 
По умолчанию все пользователи могут выполнять любые запросы на чтение (например список игр или рейтинг игры), а также выставлять свои оценки существующим играм. 

Методы API:
* /register
* /singin
* /refresh
* /validate
* /chane_role

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
* /user - получение всех своих оценок, для определения пользователя используются access token
* /user/<user_id> - получение всех оценок конкретного пользователя

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
Необходимо скачать репозиторий и подтянуть необходимые подмодули:
```
git clone --recursive https://github.com/asanikushin/game-collection.git
```
Если уже склонировали репозиторий, то:
```shell script
git submodule init
git submodule update
```

Для запуска досточно:
```shell script
docker-compose up
```
Он сам скачает и соберет нужные образы. Если требуется запустить после изменения код (например обновление репозитория), то надо указать флаг `--build` в последней команде