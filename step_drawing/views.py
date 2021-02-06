from django.http import JsonResponse, Http404
from django.views import View
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from step_drawing.models import PostStepDrawingModel, CategoryStepDrawingModel


class Home(View):

    template_name = 'front/step_drawing.html'

    def get(self, request):
        context = {
            'posts': PostStepDrawingModel.objects.filter(show_main=True, enabled=True)
        }
        return render(request, self.template_name, context)


class CategoryOrPost(View):

    first_page = 1
    posts_in_page = 34

    template_post = 'post_step/post.html'
    template_category = 'category_step/category.html'

    def get(self, request, slug):
        categories = CategoryStepDrawingModel.objects.filter(slug=slug).get_descendants(include_self=True)
        if categories:
            active_page = request.GET.get('page', self.first_page)
            posts = PostStepDrawingModel.objects\
                .filter(categories__slug=slug, enabled=True)\
                .order_by('main_category__position', '-created_at')
            p = Paginator(posts, self.posts_in_page)
            page = p.page(active_page)
            context = {
                'category': categories.first(),
                'categories': categories,
                'posts': page.object_list,
                'page_range': p.page_range,
                'active_page': active_page,
                'page': page
            }
            return render(request, self.template_category, context)
        try:
            post = PostStepDrawingModel.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise Http404()
        if post:
            post.click = int(post.click) + 1
            post.save()
            context = {
                'post': post
            }
            return render(request, self.template_post, context)
        raise Http404()


def post_step_like(request, pk):
    '''Лайкнули пост'''

    if request.method == 'POST':
        try:
            post_step = PostStepDrawingModel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'ok': False}, safe=False)
        post_step.like = int(post_step.like) + 1
        post_step.save()
        return JsonResponse({'ok': True}, safe=False)
    return JsonResponse({'ok': False}, safe=False)
