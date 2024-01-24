from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post


class PostTestCase(TestCase):
    """class for tests"""
    fixtures = ['blogging_test_fixture.json']

    def setUp(self):
        """class for setting up"""
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        """class for testing the representation of a string"""
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
