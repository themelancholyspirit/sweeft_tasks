import string
import random
from typing import Optional

from django.conf import settings
from django.http import Http404

from urlshortener.models import UrlShortener


def url_shortening(long_url: str, premium_client_string: Optional[str] = None) -> str:

    if premium_client_string:
        url_id: str = premium_client_string

        if UrlShortener.objects.filter(short_url=url_id).exists():
            raise Http404('This url id is already in database')

        if not UrlShortener.objects.filter(short_url=url_id).exists():
            UrlShortener.objects.create(original_url=long_url, short_url=url_id)
            return url_id

    SHORTCODE_MIN: int = getattr(settings, "SHORTCODE_MIN", 7)

    characters: str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    url_id: str = ''.join(random.choice(characters) for _ in range(SHORTCODE_MIN))

    if not UrlShortener.objects.filter(short_url=url_id).exists():
        UrlShortener.objects.create(original_url=long_url, short_url=url_id)
        return url_id
