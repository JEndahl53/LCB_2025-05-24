# concerts/views.py
from django.db import transaction
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import ConcertForm, ConductorForm, GuestForm, VenueForm, ConcertProgramForm
from .models import Concert, Conductor, Guest, Venue, ConcertProgram
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404


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


class ConductorCreateView(CreateView):
    model = Conductor
    template_name = "conductors/conductor_form.html"
    form_class = ConductorForm
    success_url = reverse_lazy("conductors_list")


class ConductorUpdateView(UpdateView):
    model = Conductor
    form_class = ConductorForm
    template_name = "conductors/conductor_form.html"
    success_url = reverse_lazy("conductors_list")

    def get_queryset(self):
        return Conductor.objects.all()


class ConductorDeleteView(DeleteView):
    model = Conductor
    template_name = "conductors/conductor_confirm_delete.html"
    success_url = reverse_lazy("conductors_list")

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


class GuestCreateView(CreateView):
    model = Guest
    template_name = "guests/guest_form.html"
    form_class = GuestForm
    success_url = reverse_lazy("guests_list")


class GuestUpdateView(UpdateView):
    model = Guest
    form_class = GuestForm
    template_name = "guests/guest_form.html"
    success_url = reverse_lazy("guests_list")

    def get_queryset(self):
        return Guest.objects.all()


class GuestDeleteView(DeleteView):
    model = Guest
    template_name = "guests/guest_confirm_delete.html"
    success_url = reverse_lazy("guests_list")

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


class VenueCreateView(CreateView):
    model = Venue
    template_name = "venues/venue_form.html"
    form_class = VenueForm
    success_url = reverse_lazy("venues_list")


class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = "venues/venue_form.html"
    success_url = reverse_lazy("venues_list")

    def get_queryset(self):
        return Venue.objects.all()


class VenueDeleteView(DeleteView):
    model = Venue
    template_name = "venues/venue_confirm_delete.html"
    success_url = reverse_lazy("venues_list")

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


class ConcertCreateView(CreateView):
    model = Concert
    template_name = "concerts/concert_form.html"
    form_class = ConcertForm
    success_url = reverse_lazy("concerts_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["program_formset"] = ConcertProgramFormSet(self.request.POST)
        else:
            data["program_formset"] = ConcertProgramFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        program_formset = context["formset"]

        with transaction.atomic():
            if form.is_valid() and program_formset.is_valid():
                self.object = form.save()
                program_formset.instance = self.object
                program_formset.save()
                return super().form_valid(form)
            else:
                return self.form_invalid(form)


class ConcertUpdateView(UpdateView):
    model = Concert
    form_class = ConcertForm
    template_name = "concerts/concert_form.html"
    success_url = reverse_lazy("concerts_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["program_formset"] = ConcertProgramFormSet(
                self.request.POST, instance=self.object
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
                program_formset.instance = self.object
                program_formset.save()
                return super().form_valid(form)
            else:
                return self.form_invalid(form)

    def get_queryset(self):
        return Concert.objects.all()


class ConcertDeleteView(DeleteView):
    model = Concert
    template_name = "concerts/concert_confirm_delete.html"
    success_url = reverse_lazy("concerts_list")

    def get_queryset(self):
        return Concert.objects.all()
