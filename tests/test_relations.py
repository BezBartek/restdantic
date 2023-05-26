import pytest
from django.db import connection

from pydantic_core import ValidationError

from restdantic.models import BaseModel
from restdantic.relations import LookupRelatedField
from tests.django_test_app.factories import AuthorFactory, BookFactory, GenreFactory
from tests.django_test_app.models import Author, Genre
from django.test.utils import CaptureQueriesContext

pytestmark = pytest.mark.django_db


class BookSchema(BaseModel):
    title: str
    author: Author = LookupRelatedField(lookup='id', queryset=Author.objects.all())


class BookWithGenresSchema(BaseModel):
    title: str
    genres: list[Genre] = LookupRelatedField(lookup='id', queryset=Genre.objects.all())


def test_lookup_related_field_raises_error_if_object_does_not_exist():
    with pytest.raises(ValidationError) as error:
        BookSchema(title='test', author=2)

    assert error.value.errors() == [
        {
            'ctx': {
                'error': 'Invalid id "2" - object does not exist.'
            },
            'input': 2,
            'loc': ('author',),
            'msg': 'Value error, Invalid id "2" - object does not exist.',
            'type': 'value_error',
            'url': 'https://errors.pydantic.dev/0.30.0/v/value_error'
        }
    ]


def test_lookup_related_field_returns_object_if_object_exists():
    author = AuthorFactory()
    book = BookFactory(author=author)
    schema = BookSchema(title=book.title, author=book.author.id)
    assert schema.author == author


def test_lookup_related_field_for_raises_error_if_any_object_from_list_does_not_exist():
    genre = GenreFactory()
    with pytest.raises(ValidationError) as error:
        BookWithGenresSchema(title='test', genres=[genre.id, 2, 3])

    assert error.value.errors() == [
        {
            'ctx': {
                'error': 'Invalid id(s) {2, 3} - object(s) do not exist.'
            },
            'input': [1, 2, 3],
            'loc': ('genres',),
            'msg': 'Value error, Invalid id(s) {2, 3} - object(s) do not exist.',
            'type': 'value_error',
            'url': 'https://errors.pydantic.dev/0.30.0/v/value_error'
        }
    ]


def test_lookup_related_field_returns_list_of_objects_if_all_objects_exist():
    genre1 = GenreFactory()
    genre2 = GenreFactory()
    book = BookFactory()
    schema = BookWithGenresSchema(title=book.title, genres=[genre1.id, genre2.id])
    assert schema.genres == [genre1, genre2]


def test_lookup_related_field_makes_only_one_db_query_for_list():
    genre1, genre2 = GenreFactory.create_batch(2)
    book = BookFactory()
    with CaptureQueriesContext(connection) as queries:
        schema = BookWithGenresSchema(title=book.title, genres=[genre1.id, genre2.id])
    assert schema.genres == [genre1, genre2]
    assert len(queries) == 1
