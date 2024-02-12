# homework_24.1
Структура проекта:
config/

settings.py - настройки приложений
urls.py - файл маршрутизации
celery.py - настройки Celery


admin.py - настройки админки
models.py - модели приложения
pagination.py - настройки пагинации
permissions.py - настройки прав доступа
serializers.py - сериализаторы моделей
servises.py - сервисные функции
tasks.py - задачи для Celery
tests.py - тесты
validators.py - настройки валидации
urls.py - файл маршрутизации приложения
views.py - контроллеры

manage.py - точка входа веб-приложения.

pyproject.toml - список зависимостей для проекта.


Используется виртуальное окружение poetry
Для запуска web-приложения используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.