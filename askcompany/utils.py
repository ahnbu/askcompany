import os
from uuid import uuid4
from django.utils import timezone

def uuid_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label # 앱이름
    ymd_path = timezone.now().strftime('%Y') # 2018/08/12
    uuid_name = uuid4().hex #32자리 16진수
    ext = os.path.splitext(filename)[-1].lower() #파일 확장자(소문자)
    return '/'.join([
        app_label,
        ymd_path,
        uuid_name[:2],
        uuid_name[2:4] + ext,        
    ]) #blog/2018/a7/u.jpg
    
def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label # 앱이름
    clas_name = instance.__class__.__name__.lower() # 클래스이름(소문자)
    ymd_path = timezone.now().strftime('%Y/%m/%d') # 2018/08/12
    uuid_name = uuid4().hex #32자리 16진수
    extension = os.path.splitext(filename)[-1].lower() #파일 확장자(소문자)
    return '/'.join([ # 윈도우라고 해도 /로 써도 됨
        app_label,
        clas_name,
        ymd_path,
        uuid_name[:2],
        uuid_name + extension,        
    ]) #blog/post/2018/08/12/a7/u8abcd....a7.jpg

