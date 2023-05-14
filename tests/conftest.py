from django.conf import settings


pytest_plugins = ()


def pytest_configure():
    """Configure a django settings"""
    sqlite = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'restdantic'
    }

    settings.configure(
        DATABASES={
            "default": sqlite,
        },
        ROOT_URLCONF="tests.django_test_app.urls",
        SECRET_KEY="xyz",
        INSTALLED_APPS=[
            "restdantic",
            "tests.django_test_app"
        ],
        REST_FRAMEWORK={
            'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
            'UNAUTHENTICATED_USER': None
        }
    )
