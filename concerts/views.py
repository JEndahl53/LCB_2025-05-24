# concerts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .forms import ConcertForm, ConductorForm, GuestForm, VenueForm, ConcertProgramForm
from .models import Concert, Conductor, Guest, Venue, ConcertProgram
from library.models import Music  # Import Music model
from django.urls import reverse_lazy

# from django.forms import inlineformset_factory


class ManageConcertsView(LoginRequiredMixin, TemplateView):
    """
    Management dashboard for concert operations - requires authentication.
    """

    template_name = "admin/manage_concerts.html"
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add statistics for the dashboard
        context["concert_count"] = Concert.objects.count()
        context["conductor_count"] = Conductor.objects.count()
        context["guest_count"] = Guest.objects.count()
        context["venue_count"] = Venue.objects.count()

        return context


# Conductor views
class ConductorListView(ListView):
    model = Conductor
    template_name = "conductors/conductors_list.html"
    context_object_name = "conductors"

    def get_queryset(self):
        return Conductor.objects.all()


class ConductorDetailView(DetailView):
    model = Conductor
    template_name = "conductors/conductor_detail.html"
    context_object_name = "conductor"

    def get_queryset(self):
        return Conductor.objects.all()


class ConductorCreateView(LoginRequiredMixin, CreateView):
    model = Conductor
    template_name = "conductors/conductor_form.html"
    form_class = ConductorForm
    success_url = reverse_lazy("conductors_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class ConductorUpdateView(LoginRequiredMixin, UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = "conductors/conductor_form.html"
    success_url = reverse_lazy("conductors_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Conductor.objects.all()


class ConductorDeleteView(LoginRequiredMixin, DeleteView):
    model = Conductor
    template_name = "conductors/conductor_confirm_delete.html"
    success_url = reverse_lazy("conductors_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Conductor.objects.all()


# Guest Views
class GuestListView(ListView):
    model = Guest
    template_name = "guests/guests_list.html"
    context_object_name = "guests"

    def get_queryset(self):
        return Guest.objects.all()


class GuestDetailView(DetailView):
    model = Guest
    template_name = "guests/guest_detail.html"
    context_object_name = "guest"

    def get_queryset(self):
        return Guest.objects.all()


class GuestCreateView(LoginRequiredMixin, CreateView):
    model = Guest
    template_name = "guests/guest_form.html"
    form_class = GuestForm
    success_url = reverse_lazy("guests_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class GuestUpdateView(LoginRequiredMixin, UpdateView):
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_form.html"
    success_url = reverse_lazy("guests_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Guest.objects.all()


class GuestDeleteView(LoginRequiredMixin, DeleteView):
    model = Guest
    template_name = "guests/guest_confirm_delete.html"
    success_url = reverse_lazy("guests_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Guest.objects.all()


# Venue views
class VenueListView(ListView):
    model = Venue
    template_name = "venues/venues_list.html"
    context_object_name = "venues"

    def get_queryset(self):
        return Venue.objects.all()


class VenueDetailView(DetailView):
    model = Venue
    template_name = "venues/venue_detail.html"
    context_object_name = "venue"

    def get_queryset(self):
        return Venue.objects.all()


class VenueCreateView(LoginRequiredMixin, CreateView):
    model = Venue
    template_name = "venues/venue_form.html"
    form_class = VenueForm
    success_url = reverse_lazy("venues_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated


class VenueUpdateView(LoginRequiredMixin, UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = "venues/venue_form.html"
    success_url = reverse_lazy("venues_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Venue.objects.all()


class VenueDeleteView(LoginRequiredMixin, DeleteView):
    model = Venue
    template_name = "venues/venue_confirm_delete.html"
    success_url = reverse_lazy("venues_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Venue.objects.all()


# Concert views
class ConcertListView(ListView):
    model = Concert
    template_name = "concerts/concerts_list.html"
    context_object_name = "concerts"

    def get_queryset(self):
        return Concert.objects.all()


class ConcertDetailView(DetailView):
    model = Concert
    template_name = "concerts/concert_detail.html"
    context_object_name = "concert"

    def get_queryset(self):
        return Concert.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the concert program items in the correct order with related music, composers, and arrangers
        program_items = (
            ConcertProgram.objects.filter(concert=self.object)
            .select_related("music")
            .prefetch_related("music__composer", "music__arranger")
            .order_by("performance_order")
        )
        context["program_items"] = program_items
        return context


# ConcertProgramFormSet = inlineformset_factory(
#     Concert, ConcertProgram, form=ConcertProgramForm, extra=3, can_delete=True
# )


def serialize_music_for_json(music_queryset):
    """
    Helper function to serialize music data with related composers and arrangers
    for JSON output in templates.
    """
    music_data = []
    for music in music_queryset:
        # Get composers data
        composers = []
        for composer in music.composer.all():
            composers.append(
                {
                    "id": composer.id,
                    "first_name": composer.first_name,
                    "last_name": composer.last_name,
                }
            )

        # Get arrangers data
        arrangers = []
        for arranger in music.arranger.all():
            arrangers.append(
                {
                    "id": arranger.id,
                    "first_name": arranger.first_name,
                    "last_name": arranger.last_name,
                }
            )

        music_data.append(
            {
                "id": music.id,
                "title": music.title,
                "composers": composers,
                "arrangers": arrangers,
                "difficulty": music.difficulty,
                "status": music.status,
                "year_published": music.year_published,
                "duration": str(music.duration) if music.duration else None,
            }
        )

    return music_data


class ConcertCreateView(LoginRequiredMixin, CreateView):
    model = Concert
    template_name = "concerts/concert_form.html"
    form_class = ConcertForm
    success_url = reverse_lazy("concerts_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_form_kwargs(self):
        """Include request.FILES in form kwargs."""
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            kwargs.update({"data": self.request.POST, "files": self.request.FILES})
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Get all conductors and guests for the selection interface
        data["all_conductors"] = list(
            Conductor.objects.order_by("last_name").values(
                "id", "first_name", "last_name", "title"
            )
        )
        data["all_guests"] = list(
            Guest.objects.order_by("last_name").values("id", "first_name", "last_name")
        )
        data["assigned_conductors"] = []  # Empty for new concerts
        data["assigned_guests"] = []  # Empty for new concerts

        # Get all music with related data for the music selection interface
        all_music_queryset = Music.objects.prefetch_related(
            "composer", "arranger"
        ).order_by("title")
        data["all_music"] = serialize_music_for_json(all_music_queryset)
        data["selected_music"] = []  # Empty for new concerts

        # if self.request.POST:
        #     data["program_formset"] = ConcertProgramFormSet(
        #         self.request.POST, self.request.FILES
        #     )
        # else:
        #     data["program_formset"] = ConcertProgramFormSet()
        return data

    def form_valid(self, form):
        # context = self.get_context_data()
        # program_formset = context["program_formset"]

        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()

                # Handle conductors
                conductor_ids = self.request.POST.getlist("conductors")
                if conductor_ids:
                    conductors = Conductor.objects.filter(id__in=conductor_ids)
                    self.object.conductor.set(conductors)

                # Handle guests
                guest_ids = self.request.POST.getlist("guests")
                if guest_ids:
                    guests = Guest.objects.filter(id__in=guest_ids)
                    self.object.guest.set(guests)

                # Handle music and music order
                music_ids = self.request.POST.getlist("music")
                music_orders = self.request.POST.getlist("music_order")

                print(f"DEBUG - Music IDs received: {music_ids}")
                print(f"DEBUG - Music Orders received: {music_orders}")

                if music_ids:
                    # Clear existing program entries
                    # ConcertProgram.objects.filter(concert=self.object).delete()

                    # Create new program entries with proper ordering
                    for music_id, order in zip(music_ids, music_orders):
                        try:
                            music = Music.objects.get(id=music_id)
                            program_item = ConcertProgram.objects.create(
                                concert=self.object,
                                music=music,
                                performance_order=int(order),
                            )
                            print(f"DEBUG - Created program entry: {program_item}")
                        except (Music.DoesNotExist, ValueError) as e:
                            print(f"DEBUG - Error creating program entry: {e}")
                            continue

                # NOTE: We're handling music separately, so we skip the program_formset.save()
                # program_formset.instance = self.object
                # program_formset.save()
                return super().form_valid(form)
            else:
                print(f"DEBUG - Form validation failed. Form errors: {form.errors}")
                return self.form_invalid(form)


class ConcertUpdateView(LoginRequiredMixin, UpdateView):
    model = Concert
    form_class = ConcertForm
    template_name = "concerts/concert_form.html"
    success_url = reverse_lazy("concerts_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_form_kwargs(self):
        """Include request.FILES in form kwargs."""
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            kwargs.update({"data": self.request.POST, "files": self.request.FILES})
        return kwargs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Get all conductors and guests for the selection interface
        data["all_conductors"] = list(
            Conductor.objects.order_by("last_name").values(
                "id", "first_name", "last_name", "title"
            )
        )
        data["all_guests"] = list(
            Guest.objects.order_by("last_name").values("id", "first_name", "last_name")
        )

        # Get currently assigned conductors and guests
        data["assigned_conductors"] = list(
            self.object.conductor.values("id", "first_name", "last_name", "title")
        )
        data["assigned_guests"] = list(
            self.object.guest.values("id", "first_name", "last_name")
        )

        # Get all music with related data for the music selection interface
        all_music_queryset = Music.objects.prefetch_related(
            "composer", "arranger"
        ).order_by("title")
        data["all_music"] = serialize_music_for_json(all_music_queryset)

        # Get currently selected music in the correct order
        existing_program = (
            ConcertProgram.objects.filter(concert=self.object)
            .select_related("music")
            .prefetch_related("music__composer", "music__arranger")
            .order_by("performance_order")
        )
        selected_music_queryset = [program.music for program in existing_program]
        data["selected_music"] = serialize_music_for_json(selected_music_queryset)

        # if self.request.POST:
        #     data["program_formset"] = ConcertProgramFormSet(
        #         self.request.POST, self.request.FILES, instance=self.object
        #     )
        # else:
        #     data["program_formset"] = ConcertProgramFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        # context = self.get_context_data()
        # program_formset = context["program_formset"]

        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()

                # Handle conductors
                conductor_ids = self.request.POST.getlist("conductors")
                conductors = (
                    Conductor.objects.filter(id__in=conductor_ids)
                    if conductor_ids
                    else []
                )
                self.object.conductor.set(conductors)

                # Handle guests
                guest_ids = self.request.POST.getlist("guests")
                guests = Guest.objects.filter(id__in=guest_ids) if guest_ids else []
                self.object.guest.set(guests)

                # Handle music and music order
                music_ids = self.request.POST.getlist("music")
                music_orders = self.request.POST.getlist("music_order")

                print(f"DEBUG - Music IDs received: {music_ids}")
                print(f"DEBUG - Music Orders received: {music_orders}")

                if music_ids:
                    # Clear existing program entries
                    ConcertProgram.objects.filter(concert=self.object).delete()

                    # Create new program entries with proper ordering
                    for music_id, order in zip(music_ids, music_orders):
                        try:
                            music = Music.objects.get(id=music_id)
                            program_item = ConcertProgram.objects.create(
                                concert=self.object,
                                music=music,
                                performance_order=int(order),
                            )
                            print(f"DEBUG - Created program item: {program_item}")
                        except (Music.DoesNotExist, ValueError) as e:
                            print(f"DEBUG - Error creating program item: {e}")
                            continue
                else:
                    print(f"DEBUG - No music IDs received, clearing all program items.")
                    # If no music is selected, clear all existing program entries
                    ConcertProgram.objects.filter(concert=self.object).delete()

                # NOTE: We're handling music separately, so we can skip these next steps
                # program_formset.instance = self.object
                # program_formset.save()

                return super().form_valid(form)
            else:
                print(f"DEBUG - Form validation failed. Form errors: {form.errors}")
                return self.form_invalid(form)

    def get_queryset(self):
        return Concert.objects.all()


class ConcertDeleteView(LoginRequiredMixin, DeleteView):
    model = Concert
    template_name = "concerts/concert_confirm_delete.html"
    success_url = reverse_lazy("concerts_list")
    login_url = reverse_lazy("home")  # redirect to home if not authenticated

    def get_queryset(self):
        return Concert.objects.all()
