from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener
from .serializers import urlShortenerSerializer

import random

# Create your views here.

@api_view(['POST'])
def makeShortURL(request):
    data = request.data
    longURL = data['longURL']

    if urlShortener.objects.filter(longURL=longURL).exists():
        obj = urlShortener.objects.get(longURL=longURL)
        shortURL = "http://localhost:8000/" + obj.shortURL
        return Response({'longURL': longURL, 'shortURL': shortURL})
        
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    shortURL = ("".join(random.sample(s, 6)))
    while urlShortener.objects.filter(shortURL=shortURL).exists():
        shortURL = ("".join(random.sample(s, 6)))

    urlShortener.objects.create(longURL=longURL, shortURL=shortURL)

    shortURL = "http://localhost:8000/" + shortURL

    return Response({'longURL': longURL, 'shortURL': shortURL})



def redirectURL(request, shortURL):
    try:
        obj = urlShortener.objects.get(shortURL=shortURL)
    except urlShortener.DoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longURL)