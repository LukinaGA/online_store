# Online store

## Описание

Интернет-магазин

## Содержание

* модули main.py и config.py в корне проекта
* папка data
* директория tests с тестами к модулям
* директория src с модулями classes.py и utils.py

Модуль **classes.py** содержит 2 класса:
```
class Product:
"""Класс для предоставления товара"""

    name: str
    description: str
    price: float
    quantity: int
    
class Category:
"""Класс для предоставления категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
```

В модуле **utils.py** реализована функция для чтения данных из JSON-файла и созания на их основе объектов классов

## Тестировние

В директории tests прописаны тесты модуля classes.py.
Также здесь есть модуль conftest.py с фикстурами для тестов.