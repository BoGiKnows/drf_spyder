# drf_spyder

Подготовка и запуск проекта:
docker-compose up -d --build  - создаем и поднимаем контейнер проекта
docker-compose exec drf_spyder python manage.py migrate --noinput  - создаём миграции в базу данных
docker-compose exec drf_spyder python manage.py createsuperuser - создаём администратора

Ендпоинты:
1. /organizations/<district_id>/
Список заведений - с условием заранее выбранного района
