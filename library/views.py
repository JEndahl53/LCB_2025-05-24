# library/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import ComposerForm, ArrangerForm
from .models import Composer, Arranger
from django.urls import reverse_lazy


# Composer Views
class ComposerListView(ListView):
    model = Composer
    template_name = "composers/composers_list.html"
    context_object_name = "composers"

    def get_queryset(self):
        return Composer.objects.all()


class ComposerDetailView(DetailView):
    model = Composer
    template_name = "composers/composer_detail.html"
    context_object_name = "composer"

    def get_queryset(self):
        return Composer.objects.all()


class ComposerCreateView(CreateView):
    model = Composer
    template_name = "composers/composer_form.html"
    form_class = ComposerForm
    success_url = reverse_lazy("composers_list")


class ComposerUpdateView(UpdateView):
    model = Composer
    form_class = ComposerForm
    template_name = "composers/composer_form.html"
    success_url = reverse_lazy("composers_list")

    def get_queryset(self):
        return Composer.objects.all()


class ComposerDeleteView(DeleteView):
    model = Composer
    template_name = "composers/composer_confirm_delete.html"
    success_url = reverse_lazy("composers_list")

    def get_queryset(self):
        return Composer.objects.all()


# Arranger Views
class ArrangerListView(ListView):
    model = Arranger
    template_name = "arrangers/arrangers_list.html"
    context_object_name = "arrangers"

    def get_queryset(self):
        return Arranger.objects.all()


class ArrangerDetailView(DetailView):
    model = Arranger
    template_name = "arrangers/arranger_detail.html"
    context_object_name = "arranger"

    def get_queryset(self):
        return Arranger.objects.all()


class ArrangerCreateView(CreateView):
    model = Arranger
    template_name = "arrangers/arranger_form.html"
    form_class = ArrangerForm
    success_url = reverse_lazy("arrangers_list")


class ArrangerUpdateView(UpdateView):
    model = Arranger
    form_class = ArrangerForm
    template_name = "arrangers/arranger_form.html"
    success_url = reverse_lazy("arrangers_list")

    def get_queryset(self):
        return Arranger.objects.all()


class ArrangerDeleteView(DeleteView):
    model = Arranger
    template_name = "arrangers/arranger_confirm_delete.html"
    success_url = reverse_lazy("arrangers_list")

    def get_queryset(self):
        return Arranger.objects.all()
