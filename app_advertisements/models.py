from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, verbose_name="Пользователь", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Обложка", upload_to="advertisements/", blank=True, null=True)
    video = models.FileField(verbose_name="Видео", upload_to="advertisements/", blank=True, null=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"advertisement(id = {self.id}, title = {self.title})"
    
    @admin.display(description="дата создания")
    def created_date(self):
 
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>",created_time)
        else:
            return self.created_at.strftime("%d:%m%y в %H:%M")

    @admin.display(description="дата обновления")
    def update_date(self):
    
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>", update_time)
        else:
            return self.update_at.strftime("%d:%m%y в %H:%M")

    @admin.display(description="Изображение")
    def image_mini(self):
        if self.image:
            return format_html("<img src='{}' style = 'width:40px;'>", self.image.url)
        
    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={"pk": self.pk})
    
    @admin.display(description="Видео")
    def video_mini(self):
        if self.video:
            return format_html("<img src='{}' style = 'width:40px;'>", self.video.url)
        

class Task(models.Model):
    title_task = models.CharField(verbose_name="Заголовок", max_length=128)
    description_task = models.TextField(verbose_name="Задание")
    created_at_task = models.DateTimeField(auto_now_add=True)
    update_at_task = models.DateTimeField(auto_now=True) 
    user = models.ForeignKey(to=User, verbose_name="Пользователь", on_delete=models.CASCADE)
    image_task = models.ImageField(verbose_name="Обложка", upload_to="advertisements/", blank=True, null=True)
    right_answer = models.CharField(verbose_name="Верный ответ",default=1, max_length=128)
    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return f"task(id = {self.id}, title = {self.title_task})"
    
    @admin.display(description="дата создания")
    def created_date_task(self):
 
        if self.created_at_task.date() == timezone.now().date():
            created_time_task = self.created_at_task.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>",created_time_task)
        else:
            return self.created_at_task.strftime("%d:%m%y в %H:%M")

    @admin.display(description="дата обновления")
    def update_date_task(self):
    
        if self.update_at_task.date() == timezone.now().date():
            update_time_task = self.update_at_task.time().strftime("%H:%M")
            return format_html("<span style = 'color:blue;'>Сегодня в {} </span>", update_time_task)
        else:
            return self.update_at_task.strftime("%d:%m%y в %H:%M")

    @admin.display(description="Изображение")
    def image_mini_task(self):
        if self.image_task:
            return format_html("<img src='{}' style = 'width:40px;'>", self.image_task.url)
        
    def get_absolute_url(self):
        return reverse('task', kwargs={"pk": self.pk})
    
    
    


