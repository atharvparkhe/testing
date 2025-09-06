from django.test import TestCase
from app.models import Product

class ProductModelTest(TestCase):

    def test_create_product(self):
        product = Product.objects.create(
            name="Laptop",
            price=75000.50,
            description="High-end laptop"
        )
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 75000.50)
        self.assertEqual(str(product), "Laptop")
