from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from urlshortener.serializers import UrlRandomShortenerSerializer, UrlPremiumClientShortenerSerializer
from urlshortener.models import UrlShortener
from urlshortener.permissions import IsPremiumClient
from urlshortener.shortener import url_shortening


class RandomShortenedUrlView(APIView):

    def get(self, request, *args, **kwargs):

        return Response({'is_premium_client': request.user.is_premium_client})

    def post(self, request, *args, **kwargs):
        serializer = UrlRandomShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url: str = serializer.data.get('original_url')
            short_url: str = url_shortening(original_url)
            current_site = get_current_site(request)
            data = {
                "original_url": original_url,
                "generated_short_link": f"http://{current_site}/{short_url}",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PremiumClientShortenedUrlView(APIView):

    permission_classes = [IsAuthenticated, IsPremiumClient]

    def get(self, request, *args, **kwargs):
        return Response({'is_premium_client': request.user.is_premium_client})

    def post(self, request, *args, **kwargs):

        serializer = UrlPremiumClientShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url: str = serializer.data.get('original_url')
            given_string: str = serializer.data.get('given_string')

            short_url: str = url_shortening(original_url, given_string)
            current_site = get_current_site(request)
            data = {
                "original_url": original_url,
                "generated_short_link": f"http://{current_site}/{short_url}",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class RedirectUrlView(APIView):

    def get(self, request, shortened_part: str) -> 'HttpResponseRedirect':
        try:
            shortener = UrlShortener.objects.get(short_url=shortened_part)
            shortener.counter += 1
            shortener.save()
            return HttpResponseRedirect(shortener.original_url)
        except:
            raise Http404('This link is broken!')
