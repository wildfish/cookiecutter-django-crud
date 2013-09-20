import factory
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Factory(factory.django.DjangoModelFactory):
    FACTORY_FOR = {{ cookiecutter.model_name }}

