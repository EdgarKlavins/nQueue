from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User
from django.conf import settings

# Create your tests here.


class CheckoutViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.client.login(username='testuser', password='testpassword')
        
    def test_checkout_page_renders(self):
        """
        Test that the checkout page renders correctly.
        """
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}  # Add product with quantity 1
        session.save()

        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')