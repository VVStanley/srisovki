from django.http import JsonResponse, Http404
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Category as CategoryModel, Post as PostModel


class Category(View):

    template_name = 'category/category.html'

    first_page = 1
    posts_in_page = 34

    def get(self,request, slug):
        categories = CategoryModel.objects.filter(slug=slug).get_descendants(include_self=True)
        if categories:
            active_page = request.GET.get('page', self.first_page)
            posts = PostModel.objects.filter(categories__slug=slug, enabled=True).order_by('main_category__position', '-created_at')
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
            return render(request, self.template_name, context)
        raise Http404()


class Post(View):

    template_name = 'post/post.html'

    def get(self, request, slug):
        try:
            post = PostModel.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise Http404()

        post.click = int(post.click) + 1
        post.save()

        some_next_post = PostModel.get.some_next(post.created_at, post.main_category)
        some_prew_post = PostModel.get.some_previous(post.created_at, post.main_category)

        context = {
            'post': post,
            'in_favorites': 'true' if request.user in post.wishlist.all() else 'false',
            'next_post': PostModel.get.next_(post.created_at, post.main_category),
            'prew_post': PostModel.get.previous(post.created_at, post.main_category),
            'some_next_prew_posts': some_prew_post + some_next_post,
            'family_categories': CategoryModel.objects.filter(posts_cat=post).first().get_family(),
        }
        return render(request, self.template_name, context)


class SearchPosts(View):

    template_name = 'search/search.html'
    posts_in_list = 50

    def get(self, request):
        search = request.GET.get('search', '')
        where = Q(name__icontains=search) | Q(name__istartswith=search)
        if len(search) > 4:
            where.add(Q(name__icontains=search[:-1]), Q.OR)
            where.add(Q(name__istartswith=search[:-1]), Q.OR)
        if len(search) > 6:
            where.add(Q(name__icontains=search[:-2]), Q.OR)
            where.add(Q(name__istartswith=search[:-2]), Q.OR)
        context = {
            'posts': PostModel.objects.filter(where, enabled=True).order_by('-created_at').distinct()[:self.posts_in_list]
        }
        return render(request, self.template_name, context)


def post_add_wishlist(request, pk):
    '''Добавляем пост в избранное'''

    if request.method == 'POST':
        try:
            post = PostModel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'ok': False}, safe=False)
        post.wishlist.add(request.user)
        post.save()
        return JsonResponse({'ok': True}, safe=False)
    return JsonResponse({'ok': False}, safe=False)


def post_remove_wishlist(request, pk):
    '''Удаляем пост из избранного'''

    if request.method == 'POST':
        try:
            post = PostModel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'ok': False}, safe=False)
        post.wishlist.remove(request.user)
        post.save()
        return JsonResponse({'ok': True}, safe=False)
    return JsonResponse({'ok': False}, safe=False)


def post_like(request, pk):
    '''Лайкнули пост'''

    if request.method == 'POST':
        try:
            post = PostModel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'ok': False}, safe=False)
        post.like = int(post.like) + 1
        post.save()
        return JsonResponse({'ok': True}, safe=False)
    return JsonResponse({'ok': False}, safe=False)
