from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
# from mylotto import views
from memo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('memo/', include('memo_app.urls')),
    url(r'^(?P<memokey>[0-9]+)/modify/$', views.modify, name='modify_memo'),
    url(r'^(?P<memokey>[0-9]+)/delete/$', views.delete, name='delete_memo'),
]

'''
### 아래는 로또 프로젝트 URL들
    path('', views.index, name='index'),
    path('lotto/', views.index, name='index_lotto'),
    path('lotto/new/', views.post, name='new_lotto'),
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name='lotto_detail'),
    path('mylotto/tocsv/', views.response_csv),
    path('mylotto/toexcel/', views.response_excel),
    path('mylotto/image/', views.response_pillow_image),
    url(r'^hello/$', views.index, name='hello'),
#    path('mylotto/', include('mylotto.urls')),
'''