# library/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from common.models import PersonBase, PersonType
from common.forms import PersonBaseForm
from .models import Composer, Arranger
from django.urls import reverse_lazy, path


# Composer Views
class ComposerListView(ListView):
    model = Composer
    template_name = "composers/composers_list.html"
    context_object_name = "composers"

    def get_queryset(self):
        return Composer.objects.filter(types__name=PersonType.COMPOSER)


class ComposerDetailView(DetailView):
    model = Composer
    template_name = "composers/composer_detail.html"
    context_object_name = "composer"

    def get_queryset(self):
        return Composer.objects.filter(types__name=PersonType.COMPOSER)


class ComposerCreateView(CreateView):
    model = Composer
    template_name = "composers/composer_form.html"
    form_class = PersonBaseForm
    success_url = reverse_lazy("composers_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Automatically add the "Composer" type to the new composer
        composer_type, _ = Composer.types.get_or_create(name=PersonType.COMPOSER)
        self.object.types.add(composer_type)
        return response


class ComposerUpdateView(UpdateView):
    model = Composer
    form_class = PersonBaseForm
    template_name = "composers/composer_form.html"
    success_url = reverse_lazy("composers_list")

    def get_queryset(self):
        return Composer.objects.filter(types__name=PersonType.COMPOSER)


class ComposerDeleteView(DeleteView):
    model = Composer
    template_name = "composers/composer_confirm_delete.html"
    success_url = reverse_lazy("composers_list")

    def get_queryset(self):
        return Composer.objects.filter(types__name=PersonType.COMPOSER)


# Arranger Views
