from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
    # forms의 ModelForm 클래스를 상속받는다.
    class Meta:
        model = GuessNumbers # GuessNumbers와 연결
        fields = ('name', 'text', 'num_lotto',)