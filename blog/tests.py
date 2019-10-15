from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

from .models import Post


class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username='Test',
            email='test@email.com',
            password="test123"
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

        def test_string_representation(self):
            post = Post(title='A sample title')
            self.assertEqual(str(post), post.title)
        

        










