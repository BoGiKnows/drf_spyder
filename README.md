# drf_spyder

Подготовка и запуск проекта: \n
docker-compose up -d --build  - создаем и поднимаем контейнер проекта
docker-compose exec drf_spyder python manage.py migrate --noinput  - создаём миграции в базу данных
docker-compose exec drf_spyder python manage.py createsuperuser - создаём администратора

Ендпоинты:
1. /organizations/<district_id>/
  Список заведений - с условием заранее выбранного района
  Настроены фильтры по категориям и поиск по названию товара/услуги

3. /company/<companie_id>/
   Подробная информация о предприятии по его айди

4. /create-goods/
   Создание товара/услуги

5. /goods/<goods_id>/
   Подробная информация о товаре/услуге по айди

Код покрыт тестами(PyTest). Доступ к ендпоинтам совершается через API Токен. Токены постоянные, создаются автоматически при создании нового пользователя. Можно посмотреть в админке.
Пример запроса с использованием токена:
curl --location 'http://127.0.0.1:8000/organizations/1' \
--header 'Authorization: Token f659a6ed010f8bfb54f207380bef2cf4c3c16063'
