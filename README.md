## Тестовое задание по реализации API сервиса на Django

_Что реализовано:_

:heavy_check_mark: вывод публичных статей для неавторизованных пользователей;

:x: авторизация пользователей с помощью Basic Auth;

:heavy_check_mark: регистрация новых пользователей с ролью "подписчик":

   - :heavy_check_mark: обязательные поля - email, пароль;
   - :heavy_check_mark: должна быть валидация email на соответствие маски email и на уникальность;
   - :heavy_check_mark: пароль должен быть не короче 8 символов и :x: содержать хотя бы одну цифру и букву любого регистра;

:heavy_check_mark: чтение закрытых статей (только для подписчиков) пользователями с
ролью "подписчик";

:heavy_check_mark: создание новых статей ролью "автор". Пользователям с ролью "подписчик" запрещено создание статей;

:heavy_check_mark: редактирование и удаление статей. Автор может удалять или редактировать только те статьи, которые он написал.


_Другие пояснения:_
- регистрация нового пользователя происходит по ссылке: https://agile-oasis-59414.herokuapp.com/register
- роль автора присваивается только через админку (https://agile-oasis-59414.herokuapp.com/admin, :key:dinae:dina123)
- локально использована SQLite, но для heroku подключена PostgreSQL

:lady_beetle: ***Обнаруженные баги:***
- после регистрации пользователь не аутентифицируется, приходится делать login \*слёзы сожаления\*;
- после регистрации нет переадресации к странице со статьями \*ну Дина, ну ёмаё\*;

Пользователь-автор: :key: jacklondon:zaxscdvf <br><br>


