📊 Крипто API с кэшированием в Redis

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-square&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%2523DD0031.svg?style=for-square&logo=redis&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-square&logo=python&logoColor=ffdd54)
![Github](https://img.shields.io/badge/github-%2523121011.svg?style=for-square&logo=github&logoColor=white)

Высокопроизводительный сервис API для получения данных о криптовалютах со встроенным кэшированием в Redis и ограничением запросов.

✨ Возможности
```
Актуальные цены криптовалют - Получение текущих цен для любой криптовалюты

Полная информация о монетах - Детальные рыночные данные с изображениями

Доступные криптовалюты - Список всех поддерживаемых монет

Кэширование в Redis - 60-секундный кэш для уменьшения внешних запросов

Ограничение запросов - 100 запросов в минуту с одного IP

Асинхронная работа - Построен на async/await для высокой производительности

RESTful API - Чистые и предсказуемые эндпоинты

Веб-интерфейс - Готовый фронтенд в одном HTML файле
```

🚀 Быстрый старт
```
Требования
Python 3.8+
Redis сервер
```

Установка
```
Клонируйте репозиторий

bash
git clone https://github.com/YOUR_USERNAME/crypto-api.git
cd crypto-api
Создайте виртуальное окружение

bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
Установите зависимости

bash
pip install fastapi uvicorn redis httpx python-dotenv
# Или используйте requirements.txt
Настройте окружение

bash
# Создайте файл .env на основе примера
echo "REDIS_URL=redis://localhost:6379" > .env
echo "CACHE_TTL=60" >> .env
echo "MAX_REQUESTS_PER_MINUTE=100" >> .env
Запустите Redis

bash
# macOS
brew install redis
brew services start redis

# Ubuntu/Debian
sudo apt install redis-server
sudo systemctl start redis

# Windows (используя WSL2)
sudo service redis-server start
Запустите приложение

bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
API будет доступен по адресу http://localhost:8000

📚 **Документация API**
После запуска посетите:
```
Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Веб-интерфейс: откройте frontend.html в браузере
```
**Эндпоинты API**

1. Получить цену криптовалюты
```
http
GET /crypto/price/{symbol}
Параметры:

symbol (string): ID криптовалюты в нижнем регистре (например, bitcoin, ethereum)

Ответ:

json
{
  "symbol": "bitcoin",
  "price": 45000.50
}
```
2. Получить полную информацию о монете
```
http
GET /crypto/all_info/{symbol}
Параметры:

symbol (string): ID криптовалюты в нижнем регистре

Ответ:

json
{
  "symbol": "bitcoin",
  "all_info": {
    "name": "Bitcoin",
    "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png",
    "current_price": 45000.50,
    "market_cap": 850000000000,
    "price_change_percentage_24h": 2.5,
    "market_cap_rank": 1,
    "total_volume": 25000000000
  }
}
```
3. Получить список доступных криптовалют
```
http
GET /crypto/symbols
Ответ:

json
{
  "symbols": ["bitcoin", "ethereum", "ripple", "cardano", "solana", ...]
}
```
🗂️ Структура проекта
```
crypto-api/
├── app/
│   ├── main.py              # FastAPI приложение
│   ├── core/
│   │   ├── config.py        # Переменные окружения
│   │   ├── redis.py         # Redis клиент
│   │   └── rate_limit.py   # Логика ограничения запросов
│   ├── services/
│   │   └── crypto.py        # Бизнес-логика
|   ├──schemas/
|   |   └── crypto.py        # pydantic схемы
│   ├── routers/
│   │   └── crypto.py        # API эндпоинты
│   └── deps/
│       ├── redis_deps.py    # Зависимости Redis
│       └── rate_limit_deps.py # Зависимости ограничения запросов
├── requirements.txt         # Зависимости
├── index.html           # Веб-интерфейс
└── README.md              # Этот файл
```

⚙️ **Конфигурация**
Файл config.py
```
REDIS_URL=redis://localhost:6379
CACHE_TTL=60
MAX_REQUESTS_PER_MINUTE=100

# Внешние API (CoinGecko)
EXT_API_PRICE_URL=https://api.coingecko.com/api/v3/simple/price
EXT_API_SYMBOLS_URL=https://api.coingecko.com/api/v3/simple/supported_vs_currencies
EXT_API_COIN_ALL_INFO_URL=https://api.coingecko.com/api/v3/coins/markets
```

📊 **Ограничение запросов**
```
Как работает
100 запросов в минуту на один IP адрес
Использует Redis для распределенного ограничения
Ключ: rate_limit:ip:{ip_address}
При превышении: HTTP 429 "Too Many Requests"
```

👨‍💻 **Автор**
OneSummon
GitHub: [OneSummon](https://github.com/OneSummon)

🙏**Благодарности**
```
CoinGecko API за данные о криптовалютах
```
