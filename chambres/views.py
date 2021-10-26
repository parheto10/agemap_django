from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LocaleSerializer
from .models import Locale

@api_view(['GET'])
def chambres(request):
    chambres = Locale.objects.all().order_by('libelle')
    serializer = LocaleSerializer(chambres, many=True)
    return Response(serializer.data)

# Create your views here.
