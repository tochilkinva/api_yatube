# api_yatube

Django REST Framework REST API tutorial project with posts and comments.

Обучающий проект по созданию REST API на Django REST Framework с постами и комментариями.

### Технологии
Python 3.7, Django 2.2.6, Django REST Framework

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/tochilkinva/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект из папки с manage.py:

```
python3 manage.py runserver
```

### Автор
Валентин
