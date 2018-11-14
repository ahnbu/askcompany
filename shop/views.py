import logging
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from .models import Item
from .forms import ItemForm

logger = logging.getLogger(__name__)
# __name__ = "shop.views"

def year_archive(request, hour):
    return HttpResponse('{}시간에 대한 내용'.format(hour))
    # 요청받는데, hour에 대한 내용을 받아서, 그 결과를 보여주겠다.

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    # GET인자로 q를 받고, 없으면 빈 문자열을 반환하겠다.

    logger.debug('query: {}'.format(q))
    # q값을 확인한다.

    if q:
    # 문자열가지고 참거짓 판단시에는 문자열 길이가 0이 아니라면
        qs = qs.filter(name__icontains=q) # , price_lt)
        # q가 대소문자 구별없이 name에 있는지 체크하고,
        # price도 xx보다 작은 값인지 필터링해준다.

    return render(request, 'shop/item_list.html', {
        'item_list': qs, 
        # item_list에 item_list를 보여주지 않고, qs라는 필터링된 결과를 보여주겠다.
        'q': q,
        # 검색창에 내가 입력한 검색어를 남겨서 보여주는 기능
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })

item_view = CreateView.as_view(model=Item, form_class=ItemForm)

item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)


# def item_new(request, item=None):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=item)
#         if form.is_valid():
#             item = form.save() # ModelForm에서 제공
#             return redirect(item)
#     else: # get요청일 때
#         form = ItemForm(instance=item)

#     return render(request, 'shop/item_form.html', {
#         'form' : form,
#     })

# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

# def item_new_old(request, item=None):
#     error_list = []
#     initial = {}

#     if request.method == 'POST':
#         data = request.POST
#         files = request.FILES

#         name = data.get('name')
#         desc = data.get('desc')
#         price = data.get('price')
#         photo = files.get('photo')
#         is_publish = data.get('is_publish') in (True, 't', 'True', '1')
#         # 4가지 중에 1가지로 넣어주세요.

#         # 유효성 검사
#         if len(name) < 2:
#             error_list.append('name을 2글자 이상 입력해주세요.')

#         if re.match(r'^[\da-zA-Z\s]+$', desc):
#             error_list.append('한글을 입력해주세요.')

#         if not error_list:
#             # 저장 시도
#             if item is None:
#                 item = Item()
#                 # None이라면, 새로운 객체를 만들고, 아니라면 객체를 수정해라
#             item.name=name
#             item.desc=desc
#             item.price=price
#             item.is_publish=is_publish

#             if photo:
#                 item.photo.save(photo.name, photo, save=False)
#             try:
#                 item.save()
#             except Exception as e:
#                 error_list.append(e)
#             else:
#                 return redirect(item) # item.get_absolute_url이 호출됨
#                 # 만약 redirect('shop:item_list')이라면, 목록으로 연결됨

#         initial = {
#             'name': name,
#             'desc': desc,
#             'price': price,
#             'photo': photo,
#             'is_publish': is_publish,
#         }

#     else:
#         if item is not None:
#             initial = {
#                 'name': item.name,
#                 'desc': item.desc,
#                 'price': item.price,
#                 'photo': item.photo,
#                 'is_publish': item.is_publish,
#             }

#     return render(request, 'shop/item_form.html', {
#         'error_list': error_list,
#         'initial': initial,
#     })

# def item_edit_old(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)