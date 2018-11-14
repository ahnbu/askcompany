from django.db import models
from django.utils import timezone

# Create your models here.
class Memos(models.Model):
    name = models.CharField(max_length = 20, db_column='이름')
    title = models.CharField(max_length = 50, db_column='제목')
    text = models.TextField(max_length = 150, db_column='내용', help_text='메모 내용은 150자 이내로 입력 가능합니다.')
    update_date = models.DateTimeField()
    priority = models.BooleanField(db_column='중요')

    def generate(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s by %s' % (self.title, self.name)