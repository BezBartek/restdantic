import factory
from .models import Author, Book, Review, Genre
from factory.django import DjangoModelFactory


class AuthorFactory(DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = factory.Faker('date_of_birth')

    class Meta:
        model = Author


class GenreFactory(DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Genre


class BookFactory(DjangoModelFactory):
    title = factory.Faker('sentence')
    author = factory.SubFactory(AuthorFactory)
    publish_date = factory.Faker('date')

    class Meta:
        model = Book


class ReviewFactory(DjangoModelFactory):
    reviewer_name = factory.Faker('name')
    book = factory.SubFactory(BookFactory)
    review_text = factory.Faker('paragraph')
    rating = factory.Faker('random_int', min=1, max=5)

    class Meta:
        model = Review
