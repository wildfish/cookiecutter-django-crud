from django_webtest import WebTest
from .factories import {{ cookiecutter.model_name }}Factory
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}Test(WebTest):
    def test_factory_create(self):
        """
        Test that we can create a model via the Factory
        """
        instance = {{ cookiecutter.model_name }}Factory.create()
        self.assertTrue(isinstance(instance, {{ cookiecutter.model_name }}))

