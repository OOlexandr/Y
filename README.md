# Y
# Опис структури:
* app/: Головна директорія для коду проекту.
  * api/: Зберігає всі API endpoints.
    * endpoints/: Конкретні модулі для кожного набору endpoints (аутентифікація, фотографії, коментарі).
  * core/: Загальні налаштування та конфігурація.
  * models/: ORM моделі для взаємодії з базою даних.
  * repositories/: Містить класи для взаємодії з базою даних, як правило, використовує models/ для CRUD операцій
  * schemas/: Pydantic моделі для валідації вхідних і вихідних даних.
  * services/: Логіка застосунку, така як аутентифікація, завантаження фото, і т.д.
  * main.py: Точка входу для FastAPI додатку.
* tests/: Модульні тести для проекта.

* Dockerfile: Для контейнеризації проекта.
* README.md: Документація та інструкції.
* requirements.txt: Залежності проекту.


## Схема структури
* PhotoShare/
* ├── app/
* │   ├── api/
* │   │   ├── endpoints/
* │   │   │   ├── authentication.py
* │   │   │   ├── photos.py
* │   │   │   └── comments.py
* │   │   └── api.py
* │   ├── core/
* │   │   ├── config.py
* │   │   └── database.py
* │   ├── models/
* │   │   ├── user.py
* │   │   ├── photo.py
* │   │   └── comment.py
* │   ├── repositories/
* │   │   ├── comments.py
* │   │   ├── images.py
* │   │   ├── ratings.py
* │   │   ├── tags.py
* │   │   └── users.py
* │   ├── schemas/
* │   │   ├── user.py
* │   │   ├── photo.py
* │   │   └── comment.py
* │   ├── services/
* │   │   ├── auth_service.py
* │   │   └── photo_service.py
* │   └── main.py
* ├── tests/
* │   ├── test_auth.py
* │   ├── test_photos.py
* │   └── test_comments.py
* ├── pyproject.toml
* ├── Dockerfile
* ├── requirements.txt
* └── README.md


## Хто це робив
* [Denys -> TM](https://github.com/DenysPhV)
* [Maksius93 -> SM](https://github.com/Maksius93)
* [Anatoliy -> Dev](https://github.com/anatoliysafonov)
* [OOlexandr -> Dev](https://github.com/OOlexandr)