from django.db import connection
from django.test import TestCase

class DatabaseConnectionTest(TestCase):
    def test_db_connection(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            row = cursor.fetchone()
            self.assertEqual(row[0], 1)
