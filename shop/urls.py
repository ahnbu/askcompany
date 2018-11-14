from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

app_name = 'shop'

register_converter(FourDigitYearConverter, 'year')
# 컨버터를 사용해서 year라는 형식으로 만들겠다.

urlpatterns = [
    path('article/<year:hour>/', views.year_archive),
    path('', views.item_list, name="item_list"),
    path('new/', views.item_new, name="item_new"),
    path('<int:pk>/edit/', views.item_edit, name="item_edit"),
    path('<int:pk>/', views.item_detail, name="item_detail"),
    # url에 이렇게 오면 year로 컨버팅하고, 
    # hour라는 변수에 그 값을 담아서 views.year_archive 함수에 넘기겠다.
]