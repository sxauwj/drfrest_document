# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from .models import Snippet
# from snnipets.serializers import SnippetSerializer


# def snippet_list(request):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all() # <QuerySet [<Snippet: Snippet object>, <Snippet: Snippet object>]>
#         serializer = SnippetSerializer(snippets,many=True)
#         print serializer.data
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.erros, status=400)
# def snippet_detail(request, pk):
#     try:
#         # snippet = Snippet.objects.filter(pk=pk) <QuerySet [<Snippet: Snippet object>]>
#         snippet = Snippet.objects.filter(pk=pk).first() # Snippet object
#         print snippet
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         print serializer.data
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snnipets.models import Snippet
from snnipets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.filter(pk=pk).first()
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
