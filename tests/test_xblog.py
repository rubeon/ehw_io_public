import yaml

from django.test import TestCase
from xblog.models import Post
from xblog.models import Author
from xblog.models import Category
from xblog.models import Blog
from django.contrib.auth.models import User
from django.conf import settings

class BlogTestCase(TestCase):
    """
    tests xblog functionality
    """
    def get_user(username, is_staff=True):
        """
        Returns a user, otherwise creates it and returns it
        """
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user('foo', password=username)
        return user

    def setup(self):
        # create a test user
        test_user = User.objects.create_user('test_user',
                                             password='ABC123EIEIO',
                                             is_staff=True)
        test_user.save()
        # Create a Blog
        blog = Blog.objects.create(title='My Blog',
                                owner=test_user,
                                site_id=settings.SITE_ID)
        blog.save()
        # create a test Category
        category = Category.objects.create(title='Test Category', blog=blog)
        # Create some posts
        with open('fixtures/test_fixtures.yaml') as fixtures:
            for record in yaml.load(fixtures):
                user = get_user(record['author'])
                post = Post.objects.create(title=record['title'],
                                           pub_date=record['pub_date'],
                                           create_date=record['pub_date'],
                                           categories=[category],
                                           blog=blog,
                                           status='publish',
                                           body=record['QUOTE']
                                           text_filter='markdown')
                post.save()
