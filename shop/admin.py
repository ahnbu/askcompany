from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    # 여러개의 항목을 보여주기 위해서
    list_display = ['pk', 'name', 'short_desc', 'price', 'created_at']
    list_display_links = ['name']
    search_fields = ['name', 'short_desc']
    list_filter = ['price', 'created_at']

    # 어떤 item(모델)이 있으면, 그 모델의 필드(text)를 20자까지 가져오겠다.
    def short_desc(self, item):
        return item.desc[:20]
