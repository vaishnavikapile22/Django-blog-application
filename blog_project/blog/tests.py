# blog/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        Post.objects.create(title='Test Post', content='Test Content', author=user)

    def test_post_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Content')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        Comment.objects.create(post=post, author=user, text='Test Comment')

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.text, 'Test Comment')
