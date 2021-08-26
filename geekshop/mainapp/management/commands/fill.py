import json
import os

from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **kwargs):
        # categories = load_from_json('categories')
        # ProductCategory.objects.all().delete()
        # cats_dict = dict()
        # for cat in categories:
        #     new_cat = ProductCategory(**cat)
        #     new_cat.save()
        #     cats_dict[cat['name']] = new_cat.id
        #
        # products = load_from_json('products')
        # Product.objects.all().delete()
        # for prod in products:
        #     _category = ProductCategory.objects.get(name=prod["category"])
        #     prod['category'] = _category
        #     new_prod = Product(**prod)
        #     new_prod.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=33)
