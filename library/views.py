# library/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import (
    ComposerForm,
    ArrangerForm,
    GenreForm,
    PublisherForm,
    LoaningOrganizationForm,
    BorrowingOrganizationForm,
    RentingOrganizationForm,
    MusicForm,
)
from .models import (
    Composer,
    Arranger,
    Genre,
    Publisher,
    LoaningOrganization,
    BorrowingOrganization,
    RentingOrganization,
    Music,
)
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin

# for javascript searches
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers
import json


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


# Genre Views
class GenreListView(ListView):
    model = Genre
    template_name = "genres/genres_list.html"
    context_object_name = "genres"

    def get_queryset(self):
        return Genre.objects.all()


class GenreDetailView(DetailView):
    model = Genre
    template_name = "genres/genre_detail.html"
    context_object_name = "genre"

    def get_queryset(self):
        return Genre.objects.all()


class GenreCreateView(CreateView):
    model = Genre
    template_name = "genres/genre_form.html"
    form_class = GenreForm
    success_url = reverse_lazy("genres_list")


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "genres/genre_form.html"
    success_url = reverse_lazy("genres_list")

    def get_queryset(self):
        return Genre.objects.all()


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "genres/genre_confirm_delete.html"
    success_url = reverse_lazy("genres_list")

    def get_queryset(self):
        return Genre.objects.all()


# Publisher Views
class PublisherListView(ListView):
    model = Publisher
    template_name = "publishers/publishers_list.html"
    context_object_name = "publishers"

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "publishers/publisher_detail.html"
    context_object_name = "publisher"

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = "publishers/publisher_form.html"
    form_class = PublisherForm
    success_url = reverse_lazy("publishers_list")


class PublisherUpdateView(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "publishers/publisher_form.html"
    success_url = reverse_lazy("publishers_list")

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = "publishers/publisher_confirm_delete.html"
    success_url = reverse_lazy("publishers_list")

    def get_queryset(self):
        return Publisher.objects.all()


# LoaningOrganization Views
class LoaningOrganizationListView(ListView):
    model = LoaningOrganization
    template_name = "organizations/loaningorganizations/loaningorganizations_list.html"
    context_object_name = "loaningorganizations"

    def get_queryset(self):
        return LoaningOrganization.objects.all()


class LoaningOrganizationDetailView(DetailView):
    model = LoaningOrganization
    template_name = "organizations/loaningorganizations/loaningorganization_detail.html"
    context_object_name = "loaningorganization"

    def get_queryset(self):
        return LoaningOrganization.objects.all()


class LoaningOrganizationCreateView(CreateView):
    model = LoaningOrganization
    template_name = "organizations/loaningorganizations/loaningorganization_form.html"
    form_class = LoaningOrganizationForm
    success_url = reverse_lazy("loaningorganizations_list")


class LoaningOrganizationUpdateView(UpdateView):
    model = LoaningOrganization
    form_class = LoaningOrganizationForm
    template_name = "organizations/loaningorganizations/loaningorganization_form.html"
    success_url = reverse_lazy("loaningorganizations_list")

    def get_queryset(self):
        return LoaningOrganization.objects.all()


class LoaningOrganizationDeleteView(DeleteView):
    model = LoaningOrganization
    template_name = (
        "organizations/loaningorganizations/loaningorganization_confirm_delete.html"
    )
    success_url = reverse_lazy("loaningorganizations_list")

    def get_queryset(self):
        return LoaningOrganization.objects.all()


# BorrowingOrganization Views
class BorrowingOrganizationListView(ListView):
    model = BorrowingOrganization
    template_name = (
        "organizations/borrowingorganizations/borrowingorganizations_list.html"
    )
    context_object_name = "borrowingorganizations"

    def get_queryset(self):
        return BorrowingOrganization.objects.all()


class BorrowingOrganizationDetailView(DetailView):
    model = BorrowingOrganization
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_detail.html"
    )
    context_object_name = "borrowingorganization"

    def get_queryset(self):
        return BorrowingOrganization.objects.all()


class BorrowingOrganizationCreateView(CreateView):
    model = BorrowingOrganization
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_form.html"
    )
    form_class = BorrowingOrganizationForm
    success_url = reverse_lazy("borrowingorganizations_list")


class BorrowingOrganizationUpdateView(UpdateView):
    model = BorrowingOrganization
    form_class = BorrowingOrganizationForm
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_form.html"
    )
    success_url = reverse_lazy("borrowingorganizations_list")

    def get_queryset(self):
        return BorrowingOrganization.objects.all()


class BorrowingOrganizationDeleteView(DeleteView):
    model = BorrowingOrganization
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_confirm_delete.html"
    )
    success_url = reverse_lazy("borrowingorganizations_list")

    def get_queryset(self):
        return BorrowingOrganization.objects.all()


# RentingOrganization Views
class RentingOrganizationListView(ListView):
    model = RentingOrganization
    template_name = "organizations/rentingorganizations/rentingorganizations_list.html"
    context_object_name = "rentingorganizations"

    def get_queryset(self):
        return RentingOrganization.objects.all()


class RentingOrganizationDetailView(DetailView):
    model = RentingOrganization
    template_name = "organizations/rentingorganizations/rentingorganization_detail.html"
    context_object_name = "rentingorganization"

    def get_queryset(self):
        return RentingOrganization.objects.all()


class RentingOrganizationCreateView(CreateView):
    model = RentingOrganization
    template_name = "organizations/rentingorganizations/rentingorganization_form.html"
    form_class = RentingOrganizationForm
    success_url = reverse_lazy("rentingorganizations_list")


class RentingOrganizationUpdateView(UpdateView):
    model = RentingOrganization
    form_class = RentingOrganizationForm
    template_name = "organizations/rentingorganizations/rentingorganization_form.html"
    success_url = reverse_lazy("rentingorganizations_list")

    def get_queryset(self):
        return RentingOrganization.objects.all()


class RentingOrganizationDeleteView(DeleteView):
    model = RentingOrganization
    template_name = (
        "organizations/rentingorganizations/rentingorganization_confirm_delete.html"
    )
    success_url = reverse_lazy("rentingorganizations_list")

    def get_queryset(self):
        return RentingOrganization.objects.all()


# Music views
class MusicListView(ListView):
    model = Music
    template_name = "music/music_list.html"
    context_object_name = "music_list"

    def get_queryset(self):
        return Music.objects.all()


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"
    context_object_name = "music"

    def get_queryset(self):
        return Music.objects.all()


class MusicCreateView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = "music/music_form.html"
    success_url = reverse_lazy("music_list")

    def form_valid(self, form):
        # Save the main form first
        music_instance = form.save(commit=False)
        music_instance.save()

        # Handle many-to-many relationships manually using POST data
        composer_ids = self.request.POST.getlist("composer")
        arranger_ids = self.request.POST.getlist("arranger")
        genre_ids = self.request.POST.getlist("genre")

        # Set the relationships explicitly
        music_instance.composer.set(composer_ids if composer_ids else [])
        music_instance.arranger.set(arranger_ids if arranger_ids else [])
        music_instance.genre.set(genre_ids if genre_ids else [])

        # Call the parent's form_valid to handle the redirect
        self.object = music_instance
        return super(ModelFormMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all items for JavaScript
        context["all_composers"] = list(
            Composer.objects.values("id", "first_name", "last_name")
        )
        context["all_arrangers"] = list(
            Arranger.objects.values("id", "first_name", "last_name")
        )
        context["all_genres"] = list(Genre.objects.values("id", "name"))

        # For create view, no selected items initially
        context["selected_composers"] = []
        context["selected_arrangers"] = []
        context["selected_genres"] = []

        return context


class MusicUpdateView(UpdateView):
    model = Music
    form_class = MusicForm
    template_name = "music/music_form.html"
    success_url = reverse_lazy("music_list")

    def get_queryset(self):
        return Music.objects.all()

    def form_valid(self, form):
        # Save the main form first, but don't commit M2M relationships yet
        music_instance = form.save(commit=False)
        music_instance.save()

        # Handle many-to-many relationships manually using POST data
        composer_ids = self.request.POST.getlist("composer")
        arranger_ids = self.request.POST.getlist("arranger")
        genre_ids = self.request.POST.getlist("genre")

        # Set the relationships explicitly
        music_instance.composer.set(composer_ids if composer_ids else [])
        music_instance.arranger.set(arranger_ids if arranger_ids else [])
        music_instance.genre.set(genre_ids if genre_ids else [])

        # Call the parent's form_valid to handle the redirect
        self.object = music_instance
        return super(ModelFormMixin, self).form_valid(form)

    # Adding Javascript
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all composers, arrangers, and genres for the javascript
        context["all_composers"] = list(
            Composer.objects.values("id", "first_name", "last_name")
        )
        context["all_arrangers"] = list(
            Arranger.objects.values("id", "first_name", "last_name")
        )
        context["all_genres"] = list(Genre.objects.values("id", "name"))

        # for update view, get currently selected items
        context["selected_composers"] = list(
            self.object.composer.values("id", "first_name", "last_name")
        )
        context["selected_arrangers"] = list(
            self.object.arranger.values("id", "first_name", "last_name")
        )
        context["selected_genres"] = list(self.object.genre.values("id", "name"))

        return context


class MusicDeleteView(DeleteView):
    model = Music
    template_name = "music/music_confirm_delete.html"
    success_url = reverse_lazy("music_list")

    def get_queryset(self):
        return Music.objects.all()
