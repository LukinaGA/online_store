# Online store

## Описание

Интернет-магазин

## Содержание

* файл main.py
* папка data
* директория tests с тестами к модулям
* директория src с модулем classes.py

Модуль classes.py содержит 2 класса:
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

## Тестировние

В директории tests прописаны тесты модуля classes.py.
Также здесь есть модуль conftest.py с фикстурами для тестов. Code coverage - 100%