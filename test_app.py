import unittest
from app import app

class ShoppingCartTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Products', response.data)

    def test_add_to_cart(self):
        with self.app as client:
            client.get('/add/1')  # Add product with id=1
            response = client.get('/cart')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Laptop', response.data)

if __name__ == '__main__':
    unittest.main()
