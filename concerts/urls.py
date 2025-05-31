# concerts/urls.py
from django.urls import path

from common.views import HomePageView
from .views import (
    ConductorListView,
    ConductorDetailView,
    ConductorCreateView,
    ConductorUpdateView,
    ConductorDeleteView,
    GuestListView,
    GuestDetailView,
    GuestCreateView,
    GuestUpdateView,
    GuestDeleteView,
    VenueListView,
    VenueDetailView,
    VenueCreateView,
    VenueUpdateView,
    VenueDeleteView,
    ConcertListView,
    ConcertDetailView,
    ConcertCreateView,
    ConcertUpdateView,
    ConcertDeleteView,
)


urlpatterns = [
    path("conductors/", ConductorListView.as_view(), name="conductors_list"),
    path(
        "conductors/<int:pk>/", ConductorDetailView.as_view(), name="conductor_detail"
    ),
    path("conductors/create/", ConductorCreateView.as_view(), name="conductor_create"),
    path(
        "conductors/<int:pk>/update/",
        ConductorUpdateView.as_view(),
        name="conductor_update",
    ),
    path(
        "conductors/<int:pk>/delete/",
        ConductorDeleteView.as_view(),
        name="conductor_delete",
    ),
    path("guests/", GuestListView.as_view(), name="guests_list"),
    path("guests/<int:pk>/", GuestDetailView.as_view(), name="guest_detail"),
    path("guests/create/", GuestCreateView.as_view(), name="guest_create"),
    path("guests/<int:pk>/update/", GuestUpdateView.as_view(), name="guest_update"),
    path("guests/<int:pk>/delete/", GuestDeleteView.as_view(), name="guest_delete"),
    path("venues/", VenueListView.as_view(), name="venues_list"),
    path("venues/<int:pk>/", VenueDetailView.as_view(), name="venue_detail"),
    path("venues/create/", VenueCreateView.as_view(), name="venue_create"),
    path("venues/<int:pk>/update/", VenueUpdateView.as_view(), name="venue_update"),
    path("venues/<int:pk>/delete/", VenueDeleteView.as_view(), name="venue_delete"),
    path("concerts/", ConcertListView.as_view(), name="concerts_list"),
    path("concerts/<int:pk>/", ConcertDetailView.as_view(), name="concert_detail"),
    path("concerts/create/", ConcertCreateView.as_view(), name="concert_create"),
    path(
        "concerts/<int:pk>/update/", ConcertUpdateView.as_view(), name="concert_update"
    ),
    path(
        "concerts/<int:pk>/delete/", ConcertDeleteView.as_view(), name="concert_delete"
    ),
]
