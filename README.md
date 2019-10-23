# Python Templates

## Описание
Описание проекта

## Переменные окружения
Для работы сервиса нужно добавить файл `.env` в корень проекта:
```
ENV=ENV
```

## Локальный запуск
  1. `pip install -r app/requirements.txt`
  1. `web/instance/config.py`: `DEBUG=True и остальные переменные для локальных нужд`
  1. `cd web/`
  1. `export PYTHONPATH=.`
  1. `python app/main.py`

## Запуск тестов
  1. `cd web/`
  1. `pip install -r app/requirements.txt`
  1. `export PYTHONPATH=.`
  1. `pytest -v`

## Деплой
`docker-compose up --build -d`
