from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, re_path, include
from mylotto import views as lotto_views
# from memo_app import views
from portal import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('portal/', views.index, name='index'),

    path('admin/', admin.site.urls),
#    path('price/', views.price_check, name='price_check'),
    path('price/new/', views.post, name='new_price'),

#    path('portal/', include('portal.urls')),
    path('shop/', include('shop.urls')),
    path('memo/', include('memo_app.urls')),
    path('blog/', include('blog.urls')),

    path('lotto/', lotto_views.index, name='index_lotto'),
    path('lotto/new/', lotto_views.post, name='new_lotto'),
    path('lotto/tocsv/', lotto_views.response_csv),
    path('lotto/toexcel/', lotto_views.response_excel),
    path('lotto/image/', lotto_views.response_pillow_image),
]

urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)
# static는 debug가 참일 때만 추가하고, false이면 빈값줌

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

'''
### 아래는 로또 프로젝트 URL들
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name='lotto_detail'),
    url(r'^(?P<memokey>[0-9]+)/modify/$', views.modify, name='modify_memo'),
    url(r'^(?P<memokey>[0-9]+)/delete/$', views.delete, name='delete_memo'),
    url(r'^hello/$', lotto_views.index, name='hello'),

#    path('mylotto/', include('mylotto.urls')),
'''