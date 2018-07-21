import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from xblog.models import Post


def health(request):
    return HttpResponse(Post.objects.count())
