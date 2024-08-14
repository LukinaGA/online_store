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
    price: float  # приватный атрибут
    quantity: int
    
class Category:
"""Класс для предоставления категорий товаров"""

    name: str
    description: str
    products: list  # приватный атрибут
    category_count = 0
    product_count = 0
```

В классах присутствуют приватные атрибуты(Category - products, Product - price), для работы с атрибутами прописаны геттеры и сеттеры.
```commandline
@products.setter
def add_product(self, product: Product):
    self.__products.append(product)
    Category.product_count += 1


@price.setter
def price(self, new_price):
    if new_price <= 0:
        print("Цена не должна быть нулевая или отрицательная")
    else:
        self.__price = new_price
```
Для каждого класса прописан метод __str __ для строкового отображения информации в определённом формате:
```
<Название продукта>, n руб. Остаток: m шт.
<Название категории>, количество продуктов: n шт.
```
В классе Product реализована возможность складывать продукты. Итогом сложения является полная стоимость всех товаров на складе.

В модуле **utils.py** реализована функция для чтения данных из JSON-файла и созания на их основе объектов классов

## Тестировние

В директории tests прописаны тесты модулей classes.py и utils.py.
Также здесь есть модуль conftest.py с фикстурами для тестов. Coverage report: 100%