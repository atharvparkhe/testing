from rest_framework.test import APITestCase

class SmokeTest(APITestCase):
    def test_api_root(self):
        response = self.client.get("/products/")
        self.assertIn(response.status_code, [200, 301, 302, 404])
