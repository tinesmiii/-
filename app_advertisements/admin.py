from django.contrib import admin
from .models import Advertisement, Task
# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display=["id", "title", "description", "created_date", "update_date", "user", "image_mini", "video_mini"]
admin.site.register(Advertisement, AdvertisementAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title_task", "description_task", "created_date_task", "update_date_task", "user", "image_mini_task"]
admin.site.register(Task, TaskAdmin)  