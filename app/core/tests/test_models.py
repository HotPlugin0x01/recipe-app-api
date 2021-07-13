from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test for creating a user with an email"""
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test the email for a new user"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )

        self.assertEqual(user.email, email.lower())

    
    def test_invalid_user_email(self):
        """Test creating user with no emai raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')