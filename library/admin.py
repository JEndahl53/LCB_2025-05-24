from django.contrib import admin

# Register your models here.
from .models import (
    Composer,
    Arranger,
    Genre,
    Publisher,
    BorrowingOrganization,
    LoaningOrganization,
    RentingOrganization,
    Music,
)


@admin.register(Composer)
class ComposerAdmin(admin.ModelAdmin):
    """
    Admin interface for the Composer model.
    """

    list_display = (
        "first_name",
        "last_name",
        "comment",
        "birth_date",
        "death_date",
    )
    search_fields = ("first_name", "last_name")
    ordering = ("last_name",)
    list_per_page = 20


@admin.register(Arranger)
class ArrangerAdmin(admin.ModelAdmin):
    """
    Admin interface for the Arranger model.
    """

    list_display = (
        "first_name",
        "last_name",
        "comment",
        "birth_date",
        "death_date",
    )
    search_fields = ("first_name", "last_name")
    ordering = ("last_name",)
    list_per_page = 20


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Admin interface for the Genre model.
    """

    list_display = ("name", "date_added", "date_updated")
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    """
    Admin interface for the Publisher model.
    """

    list_display = (
        "name",
        "website",
    )
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20


@admin.register(BorrowingOrganization)
class BorrowingOrganizationAdmin(admin.ModelAdmin):
    """
    Admin interface for the BorrowingOrganization model.
    """

    list_display = (
        "name",
        "contact_person",
        "contact_email",
        "contact_phone",
        "notes",
    )
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20


@admin.register(LoaningOrganization)
class LoaningOrganizationAdmin(admin.ModelAdmin):
    """
    Admin interface for the LoaningOrganization model.
    """

    list_display = (
        "name",
        "contact_person",
        "contact_email",
        "contact_phone",
        "notes",
    )
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20


@admin.register(RentingOrganization)
class RentingOrganizationAdmin(admin.ModelAdmin):
    """
    Admin interface for the RentingOrganization model.
    """

    list_display = (
        "name",
        "contact_person",
        "contact_email",
        "contact_phone",
        "notes",
    )
    search_fields = ("name",)
    ordering = ("name",)
    list_per_page = 20


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    """
    Admin interface for the MusicPiece model.
    """

    list_display = (
        "title",
        "get_composer",
        "get_arranger",
        "location_drawer",
        "location_number",
        "get_genre",
        "publisher",
        "loaning_organization",
        "borrowing_organization",
        "renting_organization",
    )
    search_fields = ("title",)
    list_filter = ("composer", "arranger", "genre", "publisher")
    ordering = ("title",)
    list_per_page = 20

    def get_composer(self, obj):
        return ", ".join([composer.get_full_name() for composer in obj.composer.all()])

    get_composer.short_description = "Composer"

    def get_arranger(self, obj):
        return ", ".join([arranger.get_full_name() for arranger in obj.arranger.all()])

    get_arranger.short_description = "Arranger"

    def get_genre(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])

    get_genre.short_description = "Genre"
