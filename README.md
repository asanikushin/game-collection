# Хранилище коллекций игр
Является учебный проектом, изначально был проект https://github.com/asanikushin/shop-systems, но потом поменял тему. 

Является упрощенным клоном части фукнционала сайта [BGG](https://boardgamegeek.com/). Копируется две части: коллекции и лог (журнал) игр.

## Функционал
Пользователи могут создавать и редактировать свои коллекции игр, добавляя игры из общего списка по их `id`.
Кроме того пользователи могут выставлять играм оценки, при повторном выставлении оценки старая удаляется.

Дополнительно пользователи могут вести журнал своих игр - с кем и когда играли. Если указать других игроков, то им будет приходить уведомление при измении данных игры

## Сервисы
Графическая структура лежит [здесь](https://app.diagrams.net?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7VtLd6M2FP41PqddJAckwHjpV6aLzJlMczrNLGVbwWoBUZATe359hZBAPEyIg03SaRYEXSQB936f7kN4BOfB%2FlOMou1nusH%2BCBib%2FQguRgAAw3H4v1RyyCSm6UqJF5ONlBWCe%2FIDS6EhpTuywUmpI6PUZyQqC9c0DPGalWQojulzudsj9ct3jZCHa4L7NfLr0j%2FJhm0zqQvGhfw3TLyturPpTLIrAVKd5ZskW7Shz5oILkdwHlPKsrNgP8d%2Bqj2ll2zczZGr%2BYPFOGRdBsTfDg97h3lfIrQLk%2Bkn6z64vYJymifk7%2BQbjxbGaGKkxxk%2FN0eukMyW4jyTu%2BI4FkdDyB1xvJFvyg5KfXjDtSmbIQ35v1lMd%2BEGpw9l8BaN2ZZ6NET%2BLaURF5pc%2BBdm7CCxgHaMctGWBb68iveEPaTDr23Z%2Bl5qLfZybtE4aI07HJMAMxwrWcjiw4Pe0GZKm8VUoqXmShiK2TRFV%2FFaQnZDfF%2F2yVSRvv9Re0lRQnfxGrcYSeEexR5mLf2cHFWcj5jyN40PfFyMfcTIU%2Fk5kOSFl%2FcroMNPJHpegyTQiKSpoVDCj6aGJCDlIAOQKU64xNL6L9SRd5iJ87nE30fFWQGt7%2BouHw9n7pA4qy9YfyRc0VVA8NU2Sk93gT9dM8otMXvCMSN8Zb9FK%2Bzf0YQwQkPeZUUZowHv4KcXZmj9tyewM6d%2BOo7PBh%2FFnzbH1CdeOpalWNJBQ3fMJyGe5%2B6osFE6Fu%2FbrVTXqhoAsxHSj9qW9CrPhVOCUrTV%2FJFjnMkMygE2093WqDzV6O4qJ8KPUPUUV%2BUyYKgVgh9nPxXXe%2BQx%2BAj%2Bou4uppuAhP95IttWmcnOZGAmm3YrwwoyLQvpuyScOXpVELfexU%2FiDcx%2B2Qc7sm88aLRWY98dDyvCn8CRjidl%2FoHB%2BTdp9qRQpWAVf7rUAuGZdnWhedj2RKyZ0srQKIs3y%2Fw4F99b2d4jKa2OpLQHdYnNKdTkRouU9PhqqmEgT57yVAlo8kqUBTQg5d3ywGyWdgOOz%2FU0W%2FEFwfHSs1LiD%2FI4jfcfH3k8S8VvqpgA9CzQUDUEEQpeNMZ7jcM50blUyTQAlAfN0qw6kiWiHil%2FYd3Wzj87qi5cJcJ4U97BdKN9cVGh8He0WhH2%2BauajT9cNqEEaQ1Hvk%2BiJIXP85YwfB8hodvnGFXcTQ%2BeBVYiOwjrnsUEDa7FPZdrsd9uBavJCssAkfTm9zh%2BIlyhHY2hSLHFe%2BSlEcMs0mI5Kc3DO%2FCy0bLn5HQEhgv1P%2Bs8Fh0PbVAwuehKqc5ftVK%2BpZa69lGSkHWlzNVzgO50XEBNoxkcF4rQjbZgIK%2BQcO8516rxdZ%2BuB5B5RWXe5N9FFbZw5aYmcVtKMSILKOMHyaB%2BzW2D9YxBRfsB2WyyPBJzDqOVmC9FQ0RJyIQq7dnIXrTRWO74yMGjfJ9Fh0QLiY6S3rg2oeGWeK%2FSpc6Wl5PfpW%2BjdaGPjwmHXBUa%2BTOcjhbnTCv9dMcXOj76dQt9eQG6vOe13Y4L9fmSuuby6KR9d8MuAmug77RBLbbOWG3XCfzLCrH19tdWB9Gc%2BZ0p0zvJeVxPICw7EPCSBxGtalXojAH4uKP%2FsAZ1Hw0RuHQflTI70NZ8Q8srjVFpR26pOQWgFfBvSlPJIW90UgNsJQO9LGG2gvXCu3Jd4TZoNb9huevF%2FywQQ%2Bm9g4hb9726H8d8uaR4WfcD6%2FXd%2F9nfwv7xu2W%2F%2BxHY756J%2FZ9QgEWyYsT8LULv%2FUei1RIQGHolqG8u3NGEeTzvqulKhUzrg0%2B40uKXFbbKtHu7ygX5ns%2BXbPumP82Oy5o1G0J855KlGLOen39QzTpGJXuyh1Ztw0eJku9JhMJO64nZtJ7cf73lWtfWjmy6F8qV79RqdoUQQ1sN1K0mMlKhVMR2dVrgcHOk8FcX6277yBc2RWZ4JE%2FM3T10oe7vrw3otqenDZ8d9OjjFd5P%2FWRAs7jdYHElO7V6pQDnVJaJcQVJ2XvKUQWYahONq9%2BygcpEmR5qE%2FVVKwNNm1M9QfOEXe538MFY1yDzSOH0Mviz3J7wZ8OB8ddQrOUWnZpaerRUO%2BU8GZoc%2F8ijUi3UEy9LS63qSZ6j5XaVmbt%2Bc1mtsA3yicip5Dm6IbGlMfnBYwk04MbTkcKhhO%2BVcW2OHbsfTlVCP6sjFfrZ2uDN4ucvWffiV0Rw%2BS8%3D)

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