from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from products.models import Product, Genre
from products.forms import ProductForm

class ProductsViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_all_products_view(self):
        """Test that the all_products view renders correctly and shows all products."""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_description_view(self):
        """Test that the product_description view renders correctly for a specific product."""
        response = self.client.get(reverse('product_description', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_description.html')

    def test_add_product_view(self):
        """Test that the add_product view renders correctly and is accessible by authenticated users."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)  
        self.assertTemplateNotUsed(response, 'products/add_product.html')  

    def test_edit_product_view(self):
        """Test that the edit_product view renders correctly and is accessible by authenticated users."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302) 
        self.assertTemplateNotUsed(response, 'products/edit_product.html')  

    
    def test_add_product_form_valid_data(self):
        """Test that the ProductForm is valid with valid input data."""
        form_data = {
            'name': 'New Product',
            'description': 'Description of the new product',
            'price': 15.00,
            
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_add_product_form_invalid_data(self):
        """Test that the ProductForm is invalid with invalid input data."""
        form_data = {}  # Invalid data
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())