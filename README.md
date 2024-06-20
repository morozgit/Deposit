# Сервис REST API для расчета депозита


## Установка 

Установите [python3](https://realpython.com/installing-python/).

## Репозиторий
Клонируйте репозиторий в удобную папку.

## Виртуальное окружение
В терминале перейдите в папку с репозиторием.

### Создание виртуального окружения
```bush 
python3 -m venv venv
```

### Активация виртуального окружения Linux

```bush
source venv/bin/activate
```

### Активация виртуального окружения Windows

```bush
venv\Scripts\activate
```

### Установка библиотек

```bush 
pip3 install -r requirements.txt
```

## Запуск

Из директории с проектом запустите сайт командой.
```bush
uvicorn main:app --reload
```

## Запуск в Docker
Установить [Docker](https://www.docker.com/get-started/)

Собрать образ 
```bush
 docker build -t deposit .
```

Запустить 
```bush
docker run -d -p 80:80 deposit
```
В [Postman](https://www.postman.com/downloads/) выполнить get запрос http://127.0.0.1:80/calc_deposit с телом.

Пример тела запроса.
```bush
{
  "date": "31.01.2021",
  "period": 2,
  "amount": 20000,
  "rate": 6
}
```