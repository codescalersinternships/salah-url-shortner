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

    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    shortURL = ("".join(random.sample(s, 6)))

    urlShortener.objects.create(
        longURL = data['longURL'],
        shortURL = shortURL
    )

    longURL = data['longURL']
    shortURL = "http://localhost:8000/" + shortURL

    return Response({'longURL': longURL, 'shortURL': shortURL})



def redirectURL(request, shortURL):
    try:
        obj = urlShortener.objects.get(shortURL=shortURL)
    except urlShortener.DoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longURL)