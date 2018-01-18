# shop

[![Build Status](https://travis-ci.org/PavelButusov/shop.svg?branch=start)](https://travis-ci.org/PavelButusov/shop)
[![Coverage Status](https://coveralls.io/repos/github/pavelbutusov/shop/badge.svg?branch=master)](https://coveralls.io/github/pavelbutusov/shop?branch=master)
# Github
https://github.com/PavelButusov/shop  <-- ссылка на гитхаб(проект экзамена)

https://github.com/PavelButusov/Shop_case <-- ссылка на гитхаб(то, что делал для тренировки к экзамену с тестами, визуальной частью)

# Скачивание
```
git clone https://github.com/pavelbutusov/shop.git
cd shop
```

# Разворачивание сервера (в режиме отладки)

```
$ pipenv shell
$ ./manage.py makemigrations <-- генерируем правила инициализации базы данных
$ ./manage.py makemigrations root_app
$ ./manage.py migrate <-- инициализируем базы данных
$ ./manage.py createsuperuser <-- создаём учётку суперпользователя (если уже есть, то: admin q1w2e3r4)
$ ./manage.py runserver 8080 <-- запускаем сервер
```

Остановить сервер - ```<Ctrl> + <C>```


Выйти из виртуального окружения - ```<Ctrl> + <D>```

# Работа с магазином (клиентская часть)
Адреса в браузере:
* localhost:8080 <-- магазин (api)
* localhost:8080/admin <-- админка магазина

# Работа с API посредством утилиты curl

Запрос токена авторизации (обязательно POST-запросом!)
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"q1w2e3r4"}' http://localhost:8080/api-token-auth/

После получения токена следущим образом образом запрашиваем данные:
curl -H "Authorization: JWT <ваш_токен>" http://localhost:8080/<куда_вы_хотели>
или, если авторизация не требуется,
curl http://localhost:8080/api/<куда_вы_хотели>


API, требующий авторизации:
  http://localhost:8080/profiles/
  http://localhost:8080/orders/
  http://localhost:8080/cart/
  http://localhost:8080/products/
  
# Xenon test:
xenon —max-absolute B —max-modules A —max-average A .

# pipenv check
pipenv check



