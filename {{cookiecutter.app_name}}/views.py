from django.core.urlresolvers import reverse
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import {{ cookiecutter.model_name }}Form
from .models import {{ cookiecutter.model_name }}


class {{ cookiecutter.model_name }}CRUDView(object):
    model = {{ cookiecutter.model_name }}
    form_class = {{ cookiecutter.model_name }}Form
    paginate_by = 20

    def get_success_url(self):
        return reverse('{{ cookiecutter.model_name|lower }}_list')


class {{ cookiecutter.model_name }}List({{ cookiecutter.model_name }}CRUDView, ListView):
    pass


class {{ cookiecutter.model_name }}Create({{ cookiecutter.model_name }}CRUDView, CreateView):
    pass


class {{ cookiecutter.model_name }}Detail({{ cookiecutter.model_name }}CRUDView, DetailView):
    pass


class {{ cookiecutter.model_name }}Update({{ cookiecutter.model_name }}CRUDView, UpdateView):
    pass


class {{ cookiecutter.model_name }}Delete({{ cookiecutter.model_name }}CRUDView, DeleteView):
    pass

