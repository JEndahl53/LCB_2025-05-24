# library/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django_filters.views import FilterView

from .forms import (
    ComposerForm,
    ArrangerForm,
    GenreForm,
    PublisherForm,
    LendingOrganizationForm,
    BorrowingOrganizationForm,
    RentingOrganizationForm,
    MusicForm,
)
from .models import (
    Composer,
    Arranger,
    Genre,
    Publisher,
    LendingOrganization,
    BorrowingOrganization,
    RentingOrganization,
    Music,
)

from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from .filters import MusicFilter
from django.db.models import Case, When, Value, CharField, Min
from django.db.models.functions import Concat, Lower

# for javascript searches
from django.http import JsonResponse
from django.views.generic import View
from django.core import serializers
import json


class ManageLibraryView(LoginRequiredMixin, TemplateView):
    """
    Management dashboard for library operations - requires authentication.
    """

    template_name = "admin/manage_library.html"
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add statistics for the dashboard
        context["music_count"] = Music.objects.count()
        context["composer_count"] = Composer.objects.count()
        context["arranger_count"] = Arranger.objects.count()
        context["genre_count"] = Genre.objects.count()
        context["publisher_count"] = Publisher.objects.count()
        context["lending_org_count"] = LendingOrganization.objects.count()
        context["borrowing_org_count"] = BorrowingOrganization.objects.count()
        context["renting_org_count"] = RentingOrganization.objects.count()

        return context


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


class ComposerCreateView(LoginRequiredMixin, CreateView):
    model = Composer
    template_name = "composers/composer_form.html"
    form_class = ComposerForm
    success_url = reverse_lazy("composers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class ComposerUpdateView(LoginRequiredMixin, UpdateView):
    model = Composer
    form_class = ComposerForm
    template_name = "composers/composer_form.html"
    success_url = reverse_lazy("composers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Composer.objects.all()


class ComposerDeleteView(LoginRequiredMixin, DeleteView):
    model = Composer
    template_name = "composers/composer_confirm_delete.html"
    success_url = reverse_lazy("composers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

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


class ArrangerCreateView(LoginRequiredMixin, CreateView):
    model = Arranger
    template_name = "arrangers/arranger_form.html"
    form_class = ArrangerForm
    success_url = reverse_lazy("arrangers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class ArrangerUpdateView(LoginRequiredMixin, UpdateView):
    model = Arranger
    form_class = ArrangerForm
    template_name = "arrangers/arranger_form.html"
    success_url = reverse_lazy("arrangers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Arranger.objects.all()


class ArrangerDeleteView(LoginRequiredMixin, DeleteView):
    model = Arranger
    template_name = "arrangers/arranger_confirm_delete.html"
    success_url = reverse_lazy("arrangers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

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


class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    template_name = "genres/genre_form.html"
    form_class = GenreForm
    success_url = reverse_lazy("genres_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "genres/genre_form.html"
    success_url = reverse_lazy("genres_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Genre.objects.all()


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = "genres/genre_confirm_delete.html"
    success_url = reverse_lazy("genres_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

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


class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    template_name = "publishers/publisher_form.html"
    form_class = PublisherForm
    success_url = reverse_lazy("publishers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = "publishers/publisher_form.html"
    success_url = reverse_lazy("publishers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    template_name = "publishers/publisher_confirm_delete.html"
    success_url = reverse_lazy("publishers_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Publisher.objects.all()


# LendingOrganization Views
class LendingOrganizationListView(ListView):
    model = LendingOrganization
    template_name = "organizations/lendingorganizations/lendingorganizations_list.html"
    context_object_name = "lendingorganizations"

    def get_queryset(self):
        return LendingOrganization.objects.all()


class LendingOrganizationDetailView(DetailView):
    model = LendingOrganization
    template_name = "organizations/lendingorganizations/lendingorganization_detail.html"
    context_object_name = "lendingorganization"

    def get_queryset(self):
        return LendingOrganization.objects.all()


class LendingOrganizationCreateView(LoginRequiredMixin, CreateView):
    model = LendingOrganization
    template_name = "organizations/lendingorganizations/lendingorganization_form.html"
    form_class = LendingOrganizationForm
    success_url = reverse_lazy("lendingorganizations_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class LendingOrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = LendingOrganization
    form_class = LendingOrganizationForm
    template_name = "organizations/lendingorganizations/lendingorganization_form.html"
    success_url = reverse_lazy("lendingorganizations_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return LendingOrganization.objects.all()


class LendingOrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = LendingOrganization
    template_name = (
        "organizations/lendingorganizations/lendingorganization_confirm_delete.html"
    )
    success_url = reverse_lazy("lendingorganizations_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return LendingOrganization.objects.all()


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


class BorrowingOrganizationCreateView(LoginRequiredMixin, CreateView):
    model = BorrowingOrganization
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_form.html"
    )
    form_class = BorrowingOrganizationForm
    success_url = reverse_lazy("borrowingorganizations_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class BorrowingOrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = BorrowingOrganization
    form_class = BorrowingOrganizationForm
    template_name = (
        "organizations/borrowingorganizations/borrowingorganization_form.html"
    )
    success_url = reverse_lazy("borrowingorganizations_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

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
class MusicListView(FilterView):
    model = Music
    template_name = "music/music_list.html"
    context_object_name = "music_list"
    filterset_class = MusicFilter
    paginate_by = 20  # Add pagination for better performance

    def get_queryset(self):
        # Optimize queries with select_related and prefetch_related
        queryset = Music.objects.select_related("publisher").prefetch_related(
            "composer", "arranger", "genre"
        )

        # Handle sorting
        sort_by = self.request.GET.get("sort", "title")
        sort_order = self.request.GET.get("order", "asc")

        # Handle ManyToMany field sorting differently
        if sort_by == "composer":
            # Annotate with the "first" composer (alphabetically by last name)
            queryset = queryset.annotate(
                first_composer_name=Min(
                    Concat(
                        "composer__last_name",
                        Value(", "),
                        "composer__first_name",
                        output_field=CharField(),
                    )
                )
            )
            if sort_order == "desc":
                queryset = queryset.order_by("-first_composer_name", "title")
            else:
                queryset = queryset.order_by("first_composer_name", "title")

        elif sort_by == "arranger":
            # Annotate with the "first" arranger (alphabetically by last name)
            queryset = queryset.annotate(
                first_arranger_name=Min(
                    Concat(
                        "arranger__last_name",
                        Value(", "),
                        "arranger__first_name",
                        output_field=CharField(),
                    )
                )
            )
            if sort_order == "desc":
                queryset = queryset.order_by("-first_arranger_name", "title")
            else:
                queryset = queryset.order_by("first_arranger_name", "title")

        elif sort_by == "genre":
            # Annotate with the "first" genre (alphabetically)
            queryset = queryset.annotate(first_genre_name=Min("genre__name"))
            if sort_order == "desc":
                queryset = queryset.order_by("-first_genre_name", "title")
            else:
                queryset = queryset.order_by("first_genre_name", "title")

        else:
            # Handle non-M2M fields with the original approach

            # Define sortable fields mapping
            sort_fields = {
                "location": ["location_drawer", "location_number"],
                "title": ["title"],
                "difficulty": ["difficulty"],
                "duration": ["duration"],
                "status": ["status"],
                "score": ["score_missing"],
            }

            if sort_by in sort_fields:
                order_fields = sort_fields[sort_by]
                if sort_order == "desc":
                    order_fields = [f"-{field}" for field in order_fields]
                queryset = queryset.order_by(*order_fields, "title")
            else:
                queryset = queryset.order_by("title")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add total count for display (use base queryset without sorting annotations)
        base_queryset = Music.objects.select_related("publisher").prefetch_related(
            "composer", "arranger", "genre"
        )
        context["total_count"] = base_queryset.count()
        context["filtered_count"] = context["object_list"].count()

        # Add sorting context
        context["current_sort"] = self.request.GET.get("sort", "title")
        context["current_order"] = self.request.GET.get("order", "asc")

        # Create sort display names
        sort_display_names = {
            "location": "Location",
            "title": "Title",
            "composer": "Composer",
            "arranger": "Arranger",
            "genre": "Genre",
            "difficulty": "Difficulty",
            "duration": "Duration",
            "status": "Status",
            "score": "Score Status",
        }
        context["current_sort_display"] = sort_display_names.get(
            context["current_sort"], "Title"
        )
        return context


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
