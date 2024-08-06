import pytest

from src.classes import Product, Category


@pytest.fixture
def product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


# @pytest.fixture
# def product_2():
#     return Product(
#         name="Iphone 15",
#         description="512GB, Gray space",
#         price=210000.0,
#         quantity=8
#     )


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        ]
    )

@pytest.fixture
def category_2():
    return Category(name="Телевизоры",
                    description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    products=[Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])
