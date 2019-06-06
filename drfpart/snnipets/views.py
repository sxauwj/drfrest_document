# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Snippet
from snnipets.serializers import SnippetSerializer


def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        print serializer.data
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.erros, status=400)
def snippet_detail(request, pk):
    try:
        # snippet = Snippet.objects.filter(pk=pk) <QuerySet [<Snippet: Snippet object>]>
        snippet = Snippet.objects.filter(pk=pk).first() # Snippet object
        print snippet
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        print serializer.data
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)