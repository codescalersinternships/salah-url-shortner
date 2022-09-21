from wsgiref.util import request_uri
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener
from .serializers import urlShortenerSerializer
from django.views.decorators.csrf import csrf_exempt

import uuid

address = "http://0.0.0.0:8000/"

# Create your views here.

@api_view(['POST'])
@csrf_exempt
def makeShortURL(request):
    data = request.data
    longURL = data['longURL']

    if urlShortener.objects.filter(longURL=longURL).exists():
        obj = urlShortener.objects.get(longURL=longURL)
        return Response({'longURL': obj.longURL, 'shortURL': obj.shortURL})
        
    shortURL = address + str(uuid.uuid4())[:6]
    urlShortener.objects.create(longURL=longURL, shortURL=shortURL)

    return Response({'longURL': longURL, 'shortURL': shortURL})


@csrf_exempt
def redirectURL(request, uuid):
    shortURL = address + uuid
    try:
        obj = urlShortener.objects.get(shortURL=shortURL)
    except urlShortener.DoesNotExist:
        obj = None

    if obj is not None:
        return redirect(obj.longURL)