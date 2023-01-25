from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Product
from .serializers import ProductSerializer
  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        
        'Add': '/create',
        'view_all': '/all',
        'Update': '/update/pk/',
        'Delete': '/item/pk/'
    }
  
    return Response(api_urls)

@api_view(['POST'])
def add_product(request):
  items=ProductSerializer(data=request.data)
  if Product.objects.filter(**request.data).exists():
    raise serializers.ValidationError('Product already exists')
  if items.is_valid():
    items.save()
    return Response(items.data)
  else:
    return Response (status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
    items = Product.objects.all()
    if items:
        data = ProductSerializer(items,many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request,pk):
    item=Product.objects.get(id=pk)
    serializer=ProductSerializer(instance=item,data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def delete_item(request,pk):
    item=Product.objects.get(id=pk)
    item.delete()
    return Response("item deleted")




