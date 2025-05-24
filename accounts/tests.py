# accounts/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from django.test import Client

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .admin import CustomUserAdmin

User = get_user_model()


class MockRequest:
    """Mock request object for admin tests"""

    def __init__(self, user=None):
        self.user = user


class CustomUserModelTests(TestCase):
    """Tests for the CustomUser model"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com"
        )

        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com"
        )

    def test_create_user(self):
        """Test creating a regular user"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        """Test creating a superuser"""
        self.assertEqual(self.admin_user.username, "admin")
        self.assertEqual(self.admin_user.email, "admin@example.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)

    def test_user_str_method(self):
        """Test the string representation of the user"""
        self.assertEqual(str(self.user), "testuser")


class CustomUserCreationFormTests(TestCase):
    """Tests for the CustomUserCreationForm"""

    def test_form_meta_attributes(self):
        """Test form Meta attributes"""
        form = CustomUserCreationForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ("email", "username"))


class CustomUserChangeFormTests(TestCase):
    """Tests for the CustomUserChangeForm"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com"
        )

    def test_form_valid_data(self):
        """Test form with valid data"""
        form = CustomUserChangeForm(
            data={
                "username": "updateduser",
                "email": "updated@example.com",
            },
            instance=self.user,
        )
        self.assertTrue(form.is_valid())
        updated_user = form.save()
        self.assertEqual(updated_user.username, "updateduser")
        self.assertEqual(updated_user.email, "updated@example.com")

    def test_form_meta_attributes(self):
        """Test form Meta attributes"""
        form = CustomUserChangeForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ("email", "username"))


class CustomUserAdminTests(TestCase):
    """Tests for the CustomUserAdmin"""

    def setUp(self):
        """Set up test data"""
        self.site = AdminSite()
        self.admin = CustomUserAdmin(User, self.site)

        self.user = User.objects.create_user(
            username="testuser", email="test@example.com"
        )

    def test_admin_attributes(self):
        """Test CustomUserAdmin attributes"""
        self.assertEqual(self.admin.add_form, CustomUserCreationForm)
        self.assertEqual(self.admin.form, CustomUserChangeForm)
        self.assertEqual(self.admin.model, User)
        self.assertEqual(
            self.admin.list_display,
            ["email", "username", "is_staff", "is_active", "is_superuser"],
        )
