from io import StringIO, BytesIO
import os
import requests
from urllib.parse import quote

import pandas as pd
from PIL import Image, ImageDraw, ImageFont

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos': lottos})

#    return render(request, 'lotto/default.html', {})
    # 템플릿 파일 경로 지정
#    return HttpResponse('<h1>로또앱 index!</h1>')


####### 로또 앱 ##################################################################################333



def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, 'lotto/detail.html', {'lotto': lotto})

def post2(request):
    if request.method == "POST":
         # create a form instance and populate it with data from the request:
        form = PostForm(request.POST) #PostForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            lotto = form.save(commit = False) #lotto 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
            lotto.generate()
            return redirect('index') #url의 name을 경로대신 입력한다.
    else:
        form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'lotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
            # "Save" 버튼을 누른 후에 결과 페이지. 
            # index는 메인 페이지로 이동. new_lotto는 입력 페이지로 이동
            # reverse는 결과만 보여줌
    else:            
        form = PostForm()
        # forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'lotto/form.html', {'form': form})
        # 템플릿 파일 경로 지정, 데이터 전달



######### CSV, 이미지 처리 앱 ################################################################################


def response_csv1(request):
#    df = pd.read_csv('e:/django/askcompany/mylotto/data/test.csv')
    df = pd.read_csv('data/test.csv')
    # 경로 앞에 /는 빼야 함

    response = HttpResponse()
    df.to_csv(response)

#    encoded_filename = quote(filename)
#    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    return response

# 이렇게 하면, CSV파일 다운로드가 되긴 하나, 
# 크롬 브라우저에서 바로 보이는 문제가 있음

# 상대 경로 지정을 어떻게 해야 하나?  
# ===> settings.py에서 STATIC_ROOT 설정해야 함
# 다운로드할 수 있는 대화창 제공은 어떻게 해야 하나? 
# ===> pandas가 아니라, os로 불러오면 잘 다운로드됨.. 
# ===> pandas 처리결과를 저장한 후 아래 os모듈로 불러서 저장하도록 하면 될 듯


def response_csv3(request):
    filepath = 'data/test.csv'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'text/csv')

        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)

    return response

# 판다스 처리 후 csv 다운로드
def response_csv(request):
    df = pd.read_csv('data/test.csv', index_col='PassengerId')
    df = df.drop('Sex', axis = 1)
    df.to_csv('data/test_2.csv')

    filepath = 'data/test_2.csv'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'text/csv')

        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)

    return response

def response_excel(request):
    filepath = 'data/train_excel.xlsx'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')

        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)

    return response

def response_pillow_image(request):
    ttf_path = "C:/Windows/Fonts/malgun.ttf"

    image_url = "http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg"
    res = requests.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)

    canvas = Image.open(io).convert("RGBA")
    font = ImageFont.truetype(ttf_path, 40)
    draw = ImageDraw.Draw(canvas)

    text = "Lily"
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin
    
    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15,15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')
    return response