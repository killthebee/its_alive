# SEMrush тестовое
---
Сервис, который показывает работает ли сайт.

Введите в строке браузера
https://whatisupandwhatisdown.herokuapp.com/healthz/?hostname=(hostname)

Где (hostname) это адресс интересующего сайта. Например:

https://whatisupandwhatisdown.herokuapp.com/healthz/?hostname=https://www.youtube.com/

Если всё ок, увидите ```{"status":"up"}```

В противном случае, ```{"status":"down"}```


## Deploy

Из этой [REPO](https://github.com/killthebee/its_alive_deploy) коммиты, запушенные в мастер, автодеплоятся в Heroku благодаря GitHub Actions.

## Локальный запуск
Python3 должен быть уже установлен.

Переместитесь в папку app.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
В командной строке введите:
```
uvicorn app:app --reload
```
После чего откройте браузер и введите в строку
http://127.0.0.1:8000/healthz/?hostname=(hostname)

Где (hostname) это адресс интересующего сайта. Например:

http://127.0.0.1:8000/healthz/?hostname=https://www.youtube.com/

Если всё ок, увидите ```{"status":"up"}```

В противном случае, ```{"status":"down"}```

## ТАЙМИНГИ и ПРОБЛЕМЫ

Потратил несколько часов тыкая хостинги, Хероку оказался единственным кто готов работать сразу/даёт создать(или не блочит) акк/
принимает мою карту(или хотя бы не просит)/поддерживает ASGI.

Heroku кажется блочит часть запросов, из-за чего скрипт работает не всегда корректно. Например к яндексу и ютуб даёт кидать запросы
а к СЕМраш нет. Думаю это пофикситься привязкой карты/оплатой.

Из-за глупой ошибки долгое время не мог заставить акшон логиниться в хероку. ([REPO](https://github.com/killthebee/its_alive_deploy))

В остальном butter smooth.


## Цель кода
Решение [тестового](https://github.com/esemi/python_intern) SEMrush