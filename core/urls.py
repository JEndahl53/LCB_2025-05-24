# core/urls.py
"""
URL configuration for the core project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from neapolitan.views import CRUDView
from common.views import HomePageView  # Import the view we created in core/views.py
from library.models import (
    Music,
    RentingOrganization,
    LoaningOrganization,
    BorrowingOrganization,
    Publisher,
    Arranger,
    Genre,
)
from concerts.models import Venue, Conductor, Guest, Concert


# Neapolitan CRUDView models
class VenueView(CRUDView):
    """
    View for the Venue model.
    """

    model = Venue
    fields = ["name", "address", "city", "state", "zip_code", "map_link"]


class ConductorView(CRUDView):
    """
    View for the Conductor model.
    """

    model = Conductor
    fields = ["title", "first_name", "middle_initial", "last_name", "comment"]


class GuestView(CRUDView):
    """
    View for the Guest model.
    """

    model = Guest
    fields = ["title", "first_name", "middle_initial", "last_name", "comment"]


class ConcertView(CRUDView):
    """
    View for the Concert model.
    """

    model = Concert
    fields = [
        "title",
        "date",
        "time",
        "venue",
        "conductor",
        "guest",
        "description",
    ]


class MusicPieceView(CRUDView):
    """
    View for the MusicPiece model.
    """

    model = Music
    fields = [
        "title",
        "composer",
        "arranger",
        "location_drawer",
        "location_number",
        "genre",
        "difficulty",
        "status",
        "publisher",
        "year_published",
        "date_acquired",
        "purchase_price",
        "purchase_source",
        "loaning_organization",
        "loan_start_date",
        "expected_return_date",
        "renting_organization",
        "rental_start_date",
        "rental_end_date",
        "rental_fee",
        "duration",
        "comments",
    ]


class RentingOrganizationView(CRUDView):
    """
    View for the RentingOrganization model.
    """

    model = RentingOrganization
    fields = ["name", "contact_person", "contact_email", "contact_phone", "description"]


class LoaningOrganizationView(CRUDView):
    """
    View for the LoaningOrganization model.
    """

    model = LoaningOrganization
    fields = ["name", "contact_person", "contact_email", "contact_phone", "description"]


class BorrowingOrganizationView(CRUDView):
    """
    View for the BorrowingOrganization model.
    """

    model = BorrowingOrganization
    fields = [
        "name",
        "contact_person",
        "contact_email",
        "contact_phone",
        "description",
    ]


class PublisherView(CRUDView):
    """
    View for the Publisher model.
    """

    model = Publisher
    fields = ["name", "contact_person", "contact_email", "contact_phone", "description"]


class ArrangerView(CRUDView):
    """
    View for the Arranger model.
    """

    model = Arranger
    fields = ["title", "first_name", "middle_initial", "last_name", "comment"]


class GenreView(CRUDView):
    """
    View for the Genre model.
    """

    model = Genre
    fields = ["name", "date_added", "date_updated"]


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("django.contrib.auth.urls")),
    # Local Apps
    path("concerts/", include("concerts.urls")),
    path("library/", include("library.urls")),
]

urlpatterns += VenueView.get_urls()
urlpatterns += ConductorView.get_urls()
urlpatterns += GuestView.get_urls()
urlpatterns += ConcertView.get_urls()
urlpatterns += MusicPieceView.get_urls()
urlpatterns += RentingOrganizationView.get_urls()
urlpatterns += LoaningOrganizationView.get_urls()
urlpatterns += PublisherView.get_urls()
urlpatterns += ArrangerView.get_urls()
urlpatterns += GenreView.get_urls()
urlpatterns += RentingOrganizationView.get_urls()
urlpatterns += LoaningOrganizationView.get_urls()
urlpatterns += BorrowingOrganizationView.get_urls()
