from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(['Post'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)