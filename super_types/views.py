from os import curdir
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_types

from supers.models import Super
from supers.serializers import SuperSerializer
from .serializers import SuperTypeSerializer
from .models import SuperType
from super_types import serializers

# Create your views here.

@api_view(['GET'])
def super_type_list(request):

    super_types = SuperType.objects.all()
    serializer = SuperTypeSerializer(super_types, many=True)

    return Response(serializer.data)