"""

These are site-specific views, such as healt checks and the like.

"""

import logging

from django.http import HttpResponse
from xblog.models import Post

LOGGER = logging.getLogger(__name__)

def health(request):
    """
    trivial health-check. This could be built out a bit.
    """
    LOGGER.debug('health check requested over %s', request.scheme)
    return HttpResponse(Post.objects.count())
