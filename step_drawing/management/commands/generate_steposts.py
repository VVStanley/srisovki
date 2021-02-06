import os
import time
import random
from faker import Faker

from django.conf import settings
from django.core.management.base import BaseCommand

from utils.text import translite_slug
from step_drawing.models import \
    CategoryStepDrawingModel, PostStepDrawingModel,\
    ImagesPostDrawingModel, VideoPostModel


class Command(BaseCommand):

    help = 'Генерируем пошаговые посты и категории для step_drawing'

    fake = Faker(['ru_RU'])

    amount_cat = 1
    amount_posts = 3
    amount_step_post = 5

    rand = [1,2,3]

    # categories = []
    # categories = CategoryStepDrawingModel.objects.filter(level=0)
    categories = CategoryStepDrawingModel.objects.filter(pk=8)

    cat_menu = os.listdir(f'{settings.BASE_DIR}/faker/cat_menu/')
    cat_image = os.listdir(f'{settings.BASE_DIR}/faker/cat_image/')
    step_post_image = os.listdir(f'{settings.BASE_DIR}/faker/step_post_image/')
    step_post_main_image = os.listdir(f'{settings.BASE_DIR}/faker/step_post_main_image/')

    def generate_category(self):
        name = f'{self.fake.text(20)[:-1]} {str(time.time()).replace(".", "")[-5:]}'
        category = CategoryStepDrawingModel(
            name=name,
            enabled=True,
            text1=self.fake.paragraph(20),
            text2=self.fake.paragraph(20),
            h1=self.fake.text(20)[:-1],
            title=self.fake.paragraph(1),
            slug=translite_slug(name),
        )
        if self.categories:
            category.parent = random.choice(self.categories)
        category.save()
        category.image_menu.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/cat_menu', random.choice(self.cat_menu)), 'rb')
        )
        category.image.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/cat_image', random.choice(self.cat_image)), 'rb')
        )
        for i in range(self.amount_posts):
            self.generate_posts(category)

    def generate_posts(self, category):
        name = f'{self.fake.text(20)[:-1]} {str(time.time()).replace(".", "")[-5:]}'
        post = PostStepDrawingModel(
            enabled=True,
            main_category=category,
            name=name,
            execution_time=random.choice(['15-20 минут', '25-30 минут', '5-10 минут']),
            level=random.choice([1,2,3]),
            title=self.fake.paragraph(1),
            slug=translite_slug(name),
            text=self.fake.paragraph(20),
        )
        post.save()
        post.categories.set(category.get_ancestors(include_self=True))
        post.image.save(
            'filename.jpg',
            open(os.path.join(settings.BASE_DIR, 'faker/step_post_main_image', random.choice(self.step_post_main_image)), 'rb')
        )
        self.generate_images_and_videos_post(post)

    def generate_images_and_videos_post(self, post):
        for i in range(self.amount_step_post):
            step = ImagesPostDrawingModel(
                position=i,
                post=post,
                text_up=self.fake.paragraph(20),
                text_down=self.fake.paragraph(5),
            )
            step.save()
            step.image.save(
                'filename.jpg',
                open(os.path.join(settings.BASE_DIR, 'faker/step_post_image', random.choice(self.step_post_image)), 'rb')
            )
        if random.choice(self.rand) == 1:
            video = VideoPostModel(
                post=post,
                video=random.choice(['https://youtu.be/qgaF6bHn3fE', 'https://youtu.be/FW8Qih9xOaM',])
            )
            video.save()

    def add_arguments(self, parser):
        parser.add_argument('amount_cat', type=int, default=1)
        parser.add_argument('amount_posts', type=int, default=3)
        parser.add_argument('amount_step_post', type=int, default=5)

    def handle(self, *args, **options):
        self.amount_cat = options['amount_cat']
        self.amount_posts = options['amount_posts']
        self.amount_step_post = options['amount_step_post']
        for i in range(self.amount_cat):
            self.generate_category()
