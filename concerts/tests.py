# concerts/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .views import HomePageView


class HomePageTests(TestCase):
    """Tests for the home page view"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.url = reverse("home")  # Assuming 'home' is the name in urls.py

    def test_homepage_status_code(self):
        """Test that homepage returns a 200 status code"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        """Test that the correct template is used"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_view_class(self):
        """Test that the view is using the correct class"""
        response = self.client.get(self.url)
        self.assertEqual(
            response.resolver_match.func.__name__, HomePageView.as_view().__name__
        )


class ConcertModelsTests(TestCase):
    """
    Basic tests for future Concert models
    This is a placeholder for when you add models to the app
    """

    def test_models_import(self):
        """Test that models module can be imported"""
        try:
            from . import models

            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import models module")


class URLTests(TestCase):
    """Tests for URL routing"""

    def test_home_url_exists_at_correct_location(self):
        """Test that the home page URL exists at the correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_url_available_by_name(self):
        """Test that the home page URL is available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
