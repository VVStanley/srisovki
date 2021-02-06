from django.conf import settings
from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

from utils.arr import categories_split_in_two, parting
from front.forms import FeedbackForm
from posts.models import Category


class Home(View):

    template_name = 'front/home.html'

    def get(self, request):
        arr_one, arr_two = categories_split_in_two(Category.objects.filter(level=0))
        context = {
            'main_categories': Category.objects.filter(show_main=True, enabled=True),
            'categories_collumn1': arr_one,
            'categories_collumn2': arr_two,
        }
        return render(request, self.template_name, context)


class WhatColorize(View):

    template_name = 'front/what_colorize.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class Sitemap(View):

    template_name = 'front/sitemap.html'

    def get(self, request):
        categories_part = parting(Category.objects.filter(level=0), 4)
        context = {
            'categories_collumn1': categories_part[0] if len(categories_part) >= 1 else [],
            'categories_collumn2': categories_part[1] if len(categories_part) >= 2 else [],
            'categories_collumn3': categories_part[2] if len(categories_part) >= 3 else [],
            'categories_collumn4': categories_part[3] if len(categories_part) >= 4 else [],
            'categories': Category.objects.all()
        }
        return render(request, self.template_name, context)


class FeedBack(View):

    template_name = 'front/feedback.html'

    def get(self, request):
        context = {'form': FeedbackForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            form.save()
            send_mail(
                'Обратная связь - срисовки',
                f'''
                    Имя пользователя - {form.cleaned_data.get('name')};
                    Почта пользователя - {form.cleaned_data.get('email')};
                    Сообщение - {form.cleaned_data.get('text')};
                ''',
                settings.EMAIL_HOST_USER,
                settings.ADMINS,
                fail_silently=False,
            )
            form = FeedbackForm()
            messages.success(request, 'Мы рассмотрим ваше сообщение в ближайшее время.')
        context = {'form': form}
        return render(request, self.template_name, context)


class RightHolders(View):

    template_name = 'front/right_holders.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class CookieRules(View):

    template_name = 'front/cookie_rules.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class TermsOfUse(View):

    template_name = 'front/terms_of_use.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class WhatRegister(View):

    template_name = 'front/what_registr.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)