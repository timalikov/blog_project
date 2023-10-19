from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework import serializers

from .serializers import *


#Universal functions to handle the different requests
def handle_get_request(model, serializer, query_params=None):
    objects = model.objects.filter(**query_params) if query_params else model.objects.all()
    if objects:
        serialized_objects = serializer(objects, many=True)
        return Response(serialized_objects.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
def handle_post_request(serializer_class, data):
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
def handle_update_request(model, serializer_class, pk, data):
    try:
        instance = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializer_class(instance=instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
def handle_delete_request(model, pk):
    try:
        instance = model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    instance.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#Overview of endpoints
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Posts': '/all_posts, /create_post, /update/pk, /delete/pk',
        'Categories': '/categories, /create_category, /update_category/pk, /delete_category/pk'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_all_posts(request):
    return handle_get_request(Post, PostSerializer, request.query_params.dict())

@api_view(['POST'])
def create_post(request):
    return handle_post_request(PostSerializer, request.data)

@api_view(['POST'])
def update_post(request, pk):
    return handle_update_request(Post, PostSerializer, pk, request.data)

@api_view(['DELETE'])
def delete_post(request, pk):
    return handle_delete_request(Post, pk)

@api_view(['GET'])
def get_all_categories(request):
    return handle_get_request(Category, CategorySerializer, request.query_params.dict())

@api_view(['POST'])
def create_category(request):
    return handle_post_request(CategorySerializer, request.data)

@api_view(['POST'])
def update_category(request, pk):
    return handle_update_request(Category, CategorySerializer, pk, request.data)

@api_view(['DELETE'])
def delete_category(request, pk):
    return handle_delete_request(Category, pk)
