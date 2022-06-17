# Скрипт для редактирования Базы Данных Электронного Дневника

Скрипт предназначен для удобного редактирования Базы Данных сайта [Электронного Дневника](https://github.com/devmanorg/e-diary.git)

### Установка

Python3 должен быть предустановлен. 

Чтобы запустить скрипт необходимо скачать файл и поместить его в директории рядом с manage.py [Электронного Дневника](https://github.com/devmanorg/e-diary.git). 

Без этого скрипт работать не будет.

### Запуск

Запустите в терминале интерпретатор python, с предустановленным django, из директории с файлом manage.py следующей командой:

```
python manage.py shell
```

Чтобы запустить скрипт, импортируем его в запущенном интерпретаторе:

```
from diary_script import *
```

### Работа со скриптом


Команда для замены всех плохих оценок ученика на хорошие:
```
fix_marks('Фамилия Имя')
```


Команда для удаления всех замечаний ученика из электронного дневника:
```
remove_chastisements('Фамилия Имя')
```
Команда для создания записи похвалы ученика, по конктретному прдмету:
```
create_commendation('Фамилия Имя', 'Название предмета')
```


### Цель проекта

Проект написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
