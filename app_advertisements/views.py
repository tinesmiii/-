from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement, Task
from app_auth.models import Profile
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
     # в гет запросе смотрим был ли элемент и именем query
    # если он был - мы получим его значение, а если не было
    # то None (особенность работы get в dictionary)
    title = request.GET.get("query")
    # если есть query 
    if title:
        # применяем фильтр на объявления
        adverts = Advertisement.objects.filter(title__icontains=title)
    else:
        # получаем все записи из БД
        adverts = Advertisement.objects.all()
    
    
    context = {"adverts": adverts, "title": title}
    return render(request, "app_advertisement/index.html", context=context)




@login_required(login_url=reverse_lazy("login"))
def advertisement_post(request):
    from .forms import AdvertisementForm
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main")
            return redirect(url)  
              
    form = AdvertisementForm()
    context = {"form":form}
    return render(request, "app_advertisement/advertisement-post.html", context = context)

def mini_game(request):
    import requests
    import json

    url = "https://www.cbr-xml-daily.ru/daily_jsonp.js"

    responce = requests.get(url=url)

    data = responce.text[responce.text.index("{"):responce.text.rindex("}") + 1]

    parsed_data = json.loads(data)

    usd_value = parsed_data["Valute"]["USD"]["Value"]
    
    eur_value = parsed_data["Valute"]["EUR"]["Value"]
    
    context = {"some_info": 123, "usd": usd_value, "eur" : eur_value}
    return render(request, "app_advertisement/mini_game.html", context=context)

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {"advertisement": advertisement}
    return render(request, "app_advertisement/advertisement.html", context=context)


from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Count

def top_sellers(request):
    users = User.objects.annotate(adv_count = Count('advertisement')).order_by("-adv_count")
    context = {"users":users}
    return render(request, "app_advertisement/top-sellers.html", context=context)

def top_children(request):
    users = User.objects.annotate(task_count= Count('task')).order_by("-task_count")
    context = {"users":users}
    return render(request, "app_advertisement/top-children.html", context=context)

# def top_reshal(request):
#     users = User.objects.annotate(points_count= Count('points')).order_by("-points_count")
#     context = {"users":users}
#     return render(request, "app_advertisement/top-reshal.html", context=context)


def task_main(request):
         # в гет запросе смотрим был ли элемент и именем query
    # если он был - мы получим его значение, а если не было
    # то None (особенность работы get в dictionary)
    title_task = request.GET.get("query")
    # если есть query 
    if title_task:
        # применяем фильтр на объявления
        tasks = Task.objects.filter(title__icontains=title_task)
    else:
        # получаем все записи из БД
        tasks = Task.objects.all()
    
    
    context = {"tasks": tasks, "title": title_task}
    return render(request, "app_advertisement/tasks-main.html", context=context)
@login_required(login_url=reverse_lazy("login"))
def task(request, pk):
    answer = request.POST.get("answer")

    tasks = Task.objects.get(id=pk)
    if answer:
        if answer == tasks.right_answer: 
            text = "верно"
            # profile = Profile.objects.get(user=request.user)
            # from django.db.models import F
            # profile.points = F("points") + 1
            # profile.save()
        else:
            text = "неверно"
    else:
        text = ""
    context = {"tasks": tasks, "text" : text}
    return render(request, "app_advertisement/task.html", context=context)

@login_required(login_url=reverse_lazy("login"))
def task_post(request):
    from .forms import TaskForm
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task(**form.cleaned_data)
            task.user = request.user
            task.save()
            url = reverse("main")
            return redirect(url)  
              
    form = TaskForm()
    context = {"form":form}
    return render(request, "app_advertisement/task-post.html", context = context)

