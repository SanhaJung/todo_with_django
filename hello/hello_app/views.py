from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(reques):
    return HttpResponse("Hllo, world. Your're at the Hello Django App index.")