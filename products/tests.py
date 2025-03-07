from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from products.models import Product
from products.util.generic import get_djust_price



class ProductTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Generate a token for the user
        self.token = Token.objects.create(user=self.user)
        
        # Authenticate the user using the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create a sample product for testing
        self.product = Product.objects.create(
            name='Product 1',
            price=100.0,
            description='description',
            stock_quantity=5
        )

    def test_list_products(self):
        url = reverse('product-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.product.name)

    def test_create_product(self):
        url = reverse('product-list-create')
        data = {
            'name': 'new product',
            'price': 200.0,
            'description': 'product description',
            'stock_quantity': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_retrieve_product(self):
        url = reverse('product-details-update', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        url = reverse('product-details-update', args=[self.product.id])
        data = {
            'name': 'Updated product name',
            'price': 150.0,
            'description': 'Updated description',
            'stock_quantity': 20
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated product name')

    def test_price_adjustment(self):
        url = reverse('product-details-update', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the price is adjusted correctly based on stock_quantity
        expected_price = get_djust_price(self.product.price, self.product.stock_quantity)

        self.assertEqual(float(response.data['price']), expected_price)