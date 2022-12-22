import csv

from django.core.management.base import BaseCommand

from reviews.models import (
    Category,
    Comment,
    Genre,
    Review,
    Title,
    GenreTitle,
)
from users.models import User

FILE_MODEL = {
    'category.csv': Category,
    'genre.csv': Genre,
    'titles.csv': Title,
    'users.csv': User,
    'review.csv': Review,
    'comments.csv': Comment,
    'genre_title.csv': GenreTitle,
}


class Command(BaseCommand):

    def handle(self, *args, **options):
        for file_name, model in FILE_MODEL.items():
            with open(
                f'static/data/{file_name}',
                newline='',
                encoding='utf-8'
            ) as csv_file:
                datareader = csv.DictReader(csv_file, delimiter=',')
                if file_name == 'titles.csv':
                    for row in datareader:
                        category = Category.objects.get(pk=row.pop('category'))
                        obj = model(
                            category=category,
                            **row
                        )
                        obj.save()
                elif file_name in ['review.csv', 'comments.csv']:
                    for row in datareader:
                        user = User.objects.get(pk=row.pop('author'))
                        obj = model(
                            author=user,
                            **row
                        )
                        obj.save()
                elif file_name == 'genre_title.csv':
                    for row in datareader:
                        genre = Genre.objects.get(pk=row.pop('genre_id'))
                        title = Title.objects.get(pk=row.pop('title_id'))
                        obj = model(
                            genre_id=genre,
                            title_id=title,
                            **row
                        )
                        obj.save()
                else:
                    model.objects.bulk_create(
                        [model(**row) for row in datareader])
