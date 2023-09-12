from django.core.management import BaseCommand

from catalog.models import Category
class Command(BaseCommand):

    def handle(self, *args, **options):
#       print('Hi, Sky!')

        #Очищаем БД

        Category.objects.all().delete()


        categories = [
            {'category_name': 'Пылесосы', 'description': 'хорошо сосут'},
            {'category_name': 'Телевизоры', 'description': 'хорошо показывают новости'},
            {'category_name': 'Смартфоны', 'description': 'хорошо звонят'},
            {'category_name': 'Холодильники', 'description': 'хорошо морозят'},
            {'category_name': 'Принтеры', 'description': 'хорошо печатают'},
            {'category_name': 'микроволновые печи', 'description': 'хорошо сосут'},

        ]
        category_to_fill = []
        for category in categories:
            category_to_fill.append(Category(**category))


        # Пакетное заполнение БД

        Category.objects.bulk_create(category_to_fill)