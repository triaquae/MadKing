#_*_coding:utf-8_*_
from rest_framework import serializers
from assets import models



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventLog
        fields = ('id','user','name', 'event_type', 'detail', 'asset', 'date', 'memo')



# @csrf_exempt
# def eventlog_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         eventobjs = models.EventLog.objects.all()
#         serializer = SnippetSerializer(eventobjs, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)





@api_view(['GET', 'POST'])
def eventlog_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        eventlogs = models.EventLog.objects.all()
        serializer = SnippetSerializer(eventlogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("request",request.data)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)