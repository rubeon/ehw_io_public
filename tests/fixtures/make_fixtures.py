import sys
import csv
import os
import pprint
import yaml
import random
import datetime
import time
import itertools
import pytz

from random import randrange
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

FIXTURES_FILE = os.path.expanduser('~/Downloads/quotes_all.csv')

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def get_date():
    # gives a random date and time for blog posts
    d1 = datetime.datetime.strptime('1/1/1999 12:00 AM UTC', '%m/%d/%Y %I:%M %p %Z')
    d2 = datetime.datetime.strptime('12/31/2017 11:59 PM UTC', '%m/%d/%Y %I:%M %p %Z')

    return timezone.make_aware(random_date(d1, d2))


max_len = 0
author_counts = {}
posts = []

settings.configure()

with open('test.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in itertools.islice(reader, 10):
    # for row in reader:
        try:
            row['pub_date'] = "%s" % get_date() # .strftime('%m/%d/%Y %I:%M %p %Z')
        except pytz.exceptions.NonExistentTimeError:
            continue
        except pytz.exceptions.AmbiguousTimeError:
            continue
        row['title'] = "Sample Blog Post"
        row['author'] = str(slugify(row['AUTHOR'])).replace('-', '_')
        posts.append(row)
        if not author_counts.has_key(row['AUTHOR']):
            author_counts[row['AUTHOR']] = 0
        author_counts[row['AUTHOR']] = author_counts[row['AUTHOR']] + 1
        print len(posts)

print "Dumping YAML..."
res = yaml.dump(posts, default_flow_style=False)
with open('test.yaml', 'w') as yamlfile:
    print "Writing %d bytes..." % len(res)
    yamlfile.write(res)
print "Done"
