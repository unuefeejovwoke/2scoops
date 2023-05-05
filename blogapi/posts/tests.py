from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            body='This is a test post.'
        )

    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.body, 'This is a test post.')
