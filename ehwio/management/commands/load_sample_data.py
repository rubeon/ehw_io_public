import sys
import yaml

from django.core.management.base import BaseCommand
from datetime import datetime
from xblog.models import Post
from xblog.models import Author
from xblog.models import Category
from xblog.models import Blog
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.dateparse import parse_datetime

def get_user(username, first_name='Test', last_name='User', is_staff=True):
    """
    Returns a user, otherwise creates it and returns it
    """
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username,
                                        first_name=first_name,
                                        last_name=last_name,
                                        password=username,
                                        is_staff=is_staff,
                                        is_superuser=is_staff)
        user.author.fullname = "%s %s" % (user.first_name, user.last_name)
        user.save()
        user.author.save()
    return user

def get_category(category_name, blog):
    try:
        category = Category.objects.get(title=category_name, blog=blog)
    except Category.DoesNotExist:
        category = Category.objects.create(title=category_name, blog=blog)
        category.save()
    return category

def get_blog(blog_name, owner):
    try:
        blog = Blog.objects.get(title=blog_name, owner=owner)
    except Blog.DoesNotExist:
        blog = Blog.objects.create(title=blog_name,
                                   owner=owner,
                                   site_id=settings.SITE_ID)
        blog.save()
    return blog

def load_data(filename):
    # create a test user
    # Create a Blog
    test_user = get_user('Test', 'User')
    blog = get_blog('My Blog',test_user)
    category = get_category('Test Category', blog)

    # Create some posts
    with open(filename) as fixtures:
        for record in yaml.load(fixtures):
            print record['pub_date']
            user = get_user(record['author'], first_name=record['AUTHOR'].split()[0], last_name=record['AUTHOR'].split()[-1])
            post = Post.objects.create(title=record['title'],
                                       pub_date=parse_datetime(record['pub_date']),
                                       create_date=record['pub_date'],
                                       author=user.author,
                                       blog=blog,
                                       status='publish',
                                       text_filter='markdown',
                                       body=record['QUOTE'])
            post.save()
            post.categories.add(category)
            post.save()

class Command(BaseCommand):
    help = 'Import a YAML file containing sample entries'
    def add_arguments(self, parser):
        parser.add_argument(
            '--filename', dest='filename', required=True,
            help='the url to process',
        )
    def handle(self, *args, **options):
        filename = options['filename']
        load_data(filename)
