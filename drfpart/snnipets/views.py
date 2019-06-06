# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#
# # from django.http import HttpResponse, JsonResponse
# # from rest_framework.parsers import JSONParser
# # from .models import Snippet
# # from snnipets.serializers import SnippetSerializer
#
#
# # def snippet_list(request):
# #     if request.method == 'GET':
# #         snippets = Snippet.objects.all() # <QuerySet [<Snippet: Snippet object>, <Snippet: Snippet object>]>
# #         serializer = SnippetSerializer(snippets,many=True)
# #         print serializer.data
# #         return JsonResponse(serializer.data, safe=False)
# #     elif request.method == 'POST':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(data=data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data, status=201)
# #         return JsonResponse(serializer.erros, status=400)
# # def snippet_detail(request, pk):
# #     try:
# #         # snippet = Snippet.objects.filter(pk=pk) <QuerySet [<Snippet: Snippet object>]>
# #         snippet = Snippet.objects.filter(pk=pk).first() # Snippet object
# #         print snippet
# #     except Snippet.DoesNotExist:
# #         return HttpResponse(status=404)
# #     if request.method == 'GET':
# #         serializer = SnippetSerializer(snippet)
# #         print serializer.data
# #         return JsonResponse(serializer.data)
# #     elif request.method == 'PUT':
# #         data = JSONParser().parse(request)
# #         serializer = SnippetSerializer(snippet, data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors, status=400)
# #     elif request.method == 'DELETE':
# #         snippet.delete()
# #         return HttpResponse(status=204)

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from snnipets.models import Snippet
# from snnipets.serializers import SnippetSerializer
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.filter(pk=pk).first()
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         data = request.data
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
from snnipets.models import Snippet
from snnipets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SnippetListView(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(request.daat)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SnippetDetailView(APIView):
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            print snippet
            return snippet
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = request.data
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(instance=snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
