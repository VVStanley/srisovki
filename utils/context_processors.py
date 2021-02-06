import random

from django.contrib.auth import get_user_model

from configs.models import ReklamaAll, Metrics
from posts.models import Post, Category
from step_drawing.models import CategoryStepDrawingModel, PostStepDrawingModel

User = get_user_model()


def all_template_data(request):
    '''Данные для всех страниц сайта'''

    # Если приложение step_drawing строим основное меню из его категорий
    if 'step_drawing' in request.resolver_match.app_names:
        categories_menu = CategoryStepDrawingModel.objects.filter(enabled=True)
        posts_count = PostStepDrawingModel.objects.all().count()
        app_step_drawing = True
        color = 'bg-teal-400'
    else:
        categories_menu = Category.objects.filter(enabled=True)
        posts_count = Post.objects.all().count()
        app_step_drawing = False
        color = 'bg-blue-600'

    context = {
        'metrics': Metrics.objects.first(),  # Все метрики, аналитики
        'reklama_all': ReklamaAll.objects.first(),  # Реклама на всех страницах
        'app_step_drawing': app_step_drawing,  # Для проверки в каком приложении находимся
        'color': color,

        'sidebar_random_posts': get_random_posts(5), # Случайные посты в сайтбаре

        'posts_count': posts_count,  # Количество срисовок
        'users_count': User.objects.all().count(),  # Количество пользователей

        'categories_menu': categories_menu,  # Основное меню
    }
    return context


def get_random_posts(amount):
    '''Берем последние 100 добавленых и выбираем рандомна из них amount штук'''

    posts_id = Post.objects\
        .filter(enabled=True, user__is_superuser=True, user__is_staff=True)\
        .order_by('-created_at').values_list('id', flat=True)[:100]
    if len(posts_id) < amount:
        return []
    random_posts_id = random.sample(tuple(posts_id), amount)
    return Post.objects.filter(id__in=random_posts_id)
