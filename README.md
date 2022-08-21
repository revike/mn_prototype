Проект "MN NameProject"
=======================

Проблема 
========
Представьте, что в гибридном митинге принимают участие два
непримиримых приверженца разных вайтбордов. Один консервативно настаивает, что
нужно использовать физическую доску и транслировать её в митинг, а второй хочет
использовать виртуальный вайтборд, чтобы на нём мог работать каждый. Очевидно,
можно трансформировать реальный вайтборд в виртуальный единожды (пусть даже и в
виде изображения) после того, как первый пользователь внесёт все необходимые
правки, и работать уже с виртуальной доской. Однако, в таком случае первый
пользователь уже не сможет отслеживать дальнейшие изменения на своем физическом
вайтборде.

Вопрос 
======
Какой механизм можно предложить, чтобы офлайн-пользователь мог
отслеживать на физическом вайтборде изменения, которые вносят остальные
пользователи на виртуальный вайтборд?


Общий функционал
----------------
Описание функционала

Основные технологии
-------------------
```
* Python 3.10
* Django 4.1
* Postgresql
```
```
* Docker
* Docker Compose
```

Установка и запуск
------------------
* Переходим в директорию проекта
```
cd mn_prototype
```
* Устанавливаем зависимости
```
pip install -r requirements.txt
```
* Выполняем миграции
```
python backend/manage.py migrate
```
* Запуск
```
python manage.py runserver
```

Запуск с помощью docker-compose
-------------------------------
```
docker-compose up -d --build
```

--------------
* Документация
--------------
[http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

По умолчанию есть 2 пользователя:
1. admin admin
2. admin1 admin1