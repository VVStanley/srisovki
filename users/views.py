import time

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import UserSettingsForm, UserAddPostForm
from posts.models import Post


class Detail(LoginRequiredMixin, View):

    template_name = 'profile/detail.html'

    def get(self, request):
        context = {
            'user_posts': Post.objects.filter(user=request.user, enabled=True, user__is_superuser=False)
        }
        return render(request, self.template_name, context)


class Settings(LoginRequiredMixin, View):

    template_name = 'profile/settings.html'

    def get(self, request):
        context = {'form': UserSettingsForm(instance=request.user)}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserSettingsForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile:settings')
        context = {'form': form}
        return render(request, self.template_name, context)


class Wishlist(LoginRequiredMixin, View):

    template_name = 'profile/wishlist.html'

    def get(self, request):
        context = {
            'wishlist_posts': Post.objects.filter(wishlist=request.user, enabled=True)
        }
        return render(request, self.template_name, context)


class UserAddPost(LoginRequiredMixin, View):

    template_name = 'profile/add_post.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserAddPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.title = form.cleaned_data.get('name')
            post.h1 = form.cleaned_data.get('name')
            post.slug = str(time.time()).replace('.', '')
            post.save()
            send_mail(
                f'Картинка от пользователя - {request.user}',
                f'Название - {form.cleaned_data.get("name")}',
                settings.EMAIL_HOST_USER,
                settings.ADMINS,
                fail_silently=False, 
            )
            return JsonResponse({'ok': True})
        return JsonResponse({'ok': False, 'errors': form.errors.as_json()})
