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
from django.urls import reverse_lazy
from django.forms import inlineformset_factory


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


ConcertProgramFormSet = inlineformset_factory(
    Concert, ConcertProgram, form=ConcertProgramForm, extra=3, can_delete=True
)


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

        if self.request.POST:
            data["program_formset"] = ConcertProgramFormSet(
                self.request.POST, self.request.FILES
            )
        else:
            data["program_formset"] = ConcertProgramFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        program_formset = context["program_formset"]

        with transaction.atomic():
            if form.is_valid() and program_formset.is_valid():
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

                program_formset.instance = self.object
                program_formset.save()
                return super().form_valid(form)
            else:
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

        if self.request.POST:
            data["program_formset"] = ConcertProgramFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data["program_formset"] = ConcertProgramFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        program_formset = context["program_formset"]

        with transaction.atomic():
            if form.is_valid() and program_formset.is_valid():
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

                program_formset.instance = self.object
                program_formset.save()
                return super().form_valid(form)
            else:
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
