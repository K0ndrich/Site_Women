# позволяет давать ответы на запросы пользователя
from django.http import HttpResponse

#  from django.shortcuts import render

# Create your views here.


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):
    return HttpResponse("hello")
