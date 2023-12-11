
from django.urls import path
from .views import top_sellers, main, advertisement_detail, advertisement_post, mini_game, task_main, task, task_post, top_children
# top_reshal


urlpatterns = [
    path('', main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers"),
    path("advertisement-post/", advertisement_post, name = "advertisement-post"),
    path("mini-game/", mini_game, name = "mini-game"),
    path("advertisement/<int:pk>", advertisement_detail, name="adv-detail"),
    path("task-main/", task_main, name = "task-main"),
    path("task/<int:pk>", task, name = "task"),
    path("task-post/", task_post, name = "task-post"),
    path("top-children/", top_children, name = "top-children"),
    # path("top-reshal/", top_reshal, name = "top-reshal")
]
