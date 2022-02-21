from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.serializers import SuperTypeSerializer
from .serializers import SuperSerializer
from .models import Super
from .models import SuperType
from supers import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):

    super_types_param = request.query_params.get('type')

    supers = Super.objects.all()

    super_types = SuperType.objects.all()

    if super_types_param == 'hero':
        supers = supers.filter(super_type__type=super_types_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif super_types_param == 'villain':
        supers = supers.filter(super_type__type=super_types_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    else:
        heroes = supers.filter(super_type__type = 'Hero')
        villains = supers.filter(super_type__type = 'Villain')

        hero_serializer = SuperSerializer(heroes, many=True)
        villain_serializer = SuperSerializer(villains, many=True)

        custom_response = {
            "Heroes": hero_serializer.data,
            "Villains": villain_serializer.data
        }
        
        return Response(custom_response)


@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)