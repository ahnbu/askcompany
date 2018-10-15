from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def year_archive(request, hour):
    return HttpResponse('{}시간에 대한 내용'.format(hour))
    # 요청받는데, hour에 대한 내용을 받아서, 그 결과를 보여주겠다.
