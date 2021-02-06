import os
import time
import random
from PIL import Image
from faker import Faker

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from utils.text import translite_slug
from posts.models import Category, Post

User = get_user_model()


class Command(BaseCommand):

    help = 'Генерируем обычные посты и категории для posts'

    fake = Faker(['ru_RU'])

    post_image = os.listdir(f'{settings.BASE_DIR}/faker/post_image/')
    cat_image = os.listdir(f'{settings.BASE_DIR}/faker/cat_image/')
    cat_main_image = os.listdir(f'{settings.BASE_DIR}/faker/cat_main_image/')
    cat_menu = os.listdir(f'{settings.BASE_DIR}/faker/cat_menu/')

    def generate_category(self, categories, amount_posts=5):
        name = f'{self.fake.text(20)[:-1]} {str(time.time()).replace(".", "")[-5:]}'
        category = Category(
            name=name,
            enabled=True,
            text1=self.fake.paragraph(20),
            text2=self.fake.paragraph(20),
            h1=self.fake.text(20)[:-1],
            title=self.fake.paragraph(1),
            slug=translite_slug(name),
        )
        if categories:
            category.parent = random.choice(categories)
        category.save()
        category.image_menu.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/cat_menu', random.choice(self.cat_menu)), 'rb')
        )
        category.image.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/cat_image', random.choice(self.cat_image)), 'rb')
        )
        category.image_main.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/cat_main_image', random.choice(self.cat_main_image)), 'rb')
        )
        for i in range(amount_posts):
            self.generate_post(category)

    def generate_post(self, category):
        name = f'{self.fake.text(20)[:-1]} {str(time.time()).replace(".", "")[-5:]}'
        post = Post(
            user=User.objects.filter(is_superuser=True).first(),
            enabled=True,
            main_category=category,
            name=name,
            title=self.fake.paragraph(1),
            slug=translite_slug(name),
            text=self.fake.paragraph(20),
        )
        post.save()
        post.categories.set(category.get_ancestors(include_self=True))
        post.image.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/post_image', random.choice(self.post_image)), 'rb')
        )

    def add_arguments(self, parser):
        parser.add_argument('amount_cat', type=int, default=1)
        parser.add_argument('amount_posts', type=int, default=5)

    def handle(self, *args, **options):
        amount_cat = options['amount_cat']
        amount_posts = options['amount_posts']
        categories = []
        for i in range(amount_cat):
            # categories = Category.objects.filter(level=0)
            # categories = Category.objects.filter(pk=56)
            self.generate_category(categories, amount_posts)
