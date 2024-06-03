from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from django.contrib.auth.models import User
from django.conf import settings
from checkout.models import Order




# I have used as a guide this website https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class CheckoutViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.client.login(username='testuser', password='testpassword')
        self.bag = {str(self.product.id): 1}

    def test_checkout_page_renders(self):
        """
        This test that the checkout page is rendering correctly.
        """
        session = self.client.session
        session['bag'] = {str(self.product.id): 1} 
        session.save()

        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_cache_checkout_data_failure(self):
        """
        Test that cache_checkout_data returns a status code of 400 when data caching fails.
        """
        response = self.client.post(reverse('cache_checkout_data'))
        self.assertEqual(response.status_code, 400)

    def test_checkout_page_redirects_with_empty_bag(self):
        """
        This tests that the checkout page redirects to the products page if the bag is empty.
        This prevents users from attempting to checkout with an empty bag.
        """
        response = self.client.get(reverse('checkout'))
        self.assertRedirects(response, reverse('products'))

    

    