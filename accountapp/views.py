from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# 기존 방식
def hello_world(request):
    return render(request, 'accountapp/temp.html')


# DRF 방식
@api_view()
def hello_world_drf(request):
    return Response({"message": "Hello world drf"})
