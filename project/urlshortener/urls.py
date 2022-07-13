from django.urls import path

from urlshortener.views import RandomShortenedUrlView, RedirectUrlView, PremiumClientShortenedUrlView

app_name: str = 'url_shortener'

urlpatterns = [
    path('random_shorten/', RandomShortenedUrlView.as_view(), name='random_shortened_url'),
    path('premium/create_url/', PremiumClientShortenedUrlView.as_view(), name='premium_shortened_url'),
    path('<str:shortened_part>', RedirectUrlView.as_view(), name='redirect'),
]
