from django.shortcuts import render
# from .forms import PostForm


def index(request):
    return render(request, 'memo_app/default.html', {}) 

def modify(request, memokey): #memokey 변수를 url에서 가져온다
    if request.method == "POST":
        #수정 저장
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(request.POST, instance=memo) # 새로 입력된 인스턴스 데이터를 form 인스턴스에 새로 담는다.
        if form.is_valid():
             form.save() # 변경한 form을 저장한다 (수정, 업데이트)
             return redirect('index')
    else:
        #수정 입력
        memo = Memos.objects.get(pk = memokey) # 특정 데이터를 인스턴스에 담는다.
        form = PostForm(instance = memo) # 기존에 존재하는 데이터를 가져온다. (수정화면에 내용 포함)
        return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})

def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    memo.delete()
    return redirect('index')