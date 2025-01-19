# tests.py

from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=10.99, description="This is a test product.")

    def test_product_str(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(str(product), product.name)