from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app.models import Product

class ProductAPITests(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Tablet",
            price=15000,
            description="Android tablet"
        )
        self.list_url = reverse("product-list")
        self.detail_url = reverse("product-detail", kwargs={"id": self.product.id})

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Tablet")

    def test_retrieve_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Tablet")

    def test_create_product(self):
        data = {"name": "Monitor", "price": "12000.00", "description": "24-inch display"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        data = {"name": "Tablet Pro", "price": "20000.00", "description": "Updated tablet"}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Tablet Pro")

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
