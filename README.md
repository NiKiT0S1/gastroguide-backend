# GastroGuide Backend

Backend часть проекта **GastroGuide** — REST API сервис для мобильного приложения гастрономического навигатора по заведениям Астаны.

## Стек технологий

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic
* OpenRouteService API
* Google Gemini API
* CORS Middleware
* PostgreSQL
* Swagger

---

## Основной функционал

* Получение списка заведений
* Получение детальной информации о заведении
* AI-рекомендации заведений
* Построение маршрута до выбранного заведения
* Swagger API документация

---

## Структура проекта

```text
gastroguide-backend/
│── app/
│   │── api/
│   │── core/
│   │── models/
│   │── schemas/
│   │── services/
│   │── main.py
│
│── .gitignore
│── requirements.txt
```

---

## Запуск проекта локально

### 1. Создать виртуальное окружение

```bash
python -m venv venv
```

### 2. Активировать окружение

Windows:

```bash
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать `.env`

```env
DATABASE_URL=postgresql+psycopg2://ТВОЕ_ИМЯ:ТВОЙ_ПАРОЛЬ@localhost:5432/gastroguide_db
GEMINI_API_KEY=ваш_gemini_api_ключ
ORS_API_KEY=ваш_openrouteservice_ключ
```

### 5. Запуск backend

Для локальной работы с мобильными устройствами:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## Swagger документация

После запуска:

```text
http://127.0.0.1:8000/docs
```

Для мобильного устройства:

```text
http://ВАШ_IP:8000/docs
```

Пример:

```text
http://192.168.1.78:8000/docs
```

---

## Запуск frontend совместно с backend

Frontend должен использовать IP ноутбука:

```ts
http://192.168.1.78:8000/api/v1
```

Backend и frontend должны быть в одной Wi-Fi сети.

---

## Запуск frontend

```bash
npm start
```

или для Expo tunnel:

```bash
npm start -- --tunnel
```

---

## Основные API endpoints

### Restaurants

```text
GET /api/v1/restaurants
```

### Restaurant by id

```text
GET /api/v1/restaurants/{id}
```

### AI Assistant

```text
POST /api/v1/ai/chat
```

### Routes

```text
GET /api/v1/routes
```

---

## Текущее состояние проекта

Реализовано:

* локальная full-stack интеграция
* mobile тестирование
* маршруты
* AI чат

Не реализовано:

* аутентификация
* пользователи
* favorites persistence
* база пользователей
* Сохранение истории чата с ИИ в базе для каждого пользователя
* Подключение PostGIS и настройка координатов для каждого пользователя

---
