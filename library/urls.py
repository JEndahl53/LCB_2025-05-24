# library/urls.py
from django.urls import path

from common.views import HomePageView

from library.views import (
    ComposerListView,
    ComposerDetailView,
    ComposerCreateView,
    ComposerUpdateView,
    ComposerDeleteView,
    ArrangerListView,
    ArrangerDetailView,
    ArrangerCreateView,
    ArrangerUpdateView,
    ArrangerDeleteView,
    GenreListView,
    GenreDetailView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    PublisherListView,
    PublisherDetailView,
    PublisherCreateView,
    PublisherUpdateView,
    PublisherDeleteView,
    LendingOrganizationListView,
    LendingOrganizationDetailView,
    LendingOrganizationCreateView,
    LendingOrganizationUpdateView,
    LendingOrganizationDeleteView,
    BorrowingOrganizationListView,
    BorrowingOrganizationDetailView,
    BorrowingOrganizationCreateView,
    BorrowingOrganizationUpdateView,
    BorrowingOrganizationDeleteView,
    RentingOrganizationListView,
    RentingOrganizationDetailView,
    RentingOrganizationCreateView,
    RentingOrganizationUpdateView,
    RentingOrganizationDeleteView,
    MusicListView,
    MusicDetailView,
    MusicCreateView,
    MusicUpdateView,
    MusicDeleteView,
    ManageLibraryView,
)
from concerts.views import ManageConcertsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("managelibrary/", ManageLibraryView.as_view(), name="manage_library"),
    path(
        "concerts/manageconcerts/", ManageConcertsView.as_view(), name="manage_concerts"
    ),
    path("composers/", ComposerListView.as_view(), name="composers_list"),
    path(
        "composers/<int:pk>/",
        ComposerDetailView.as_view(),
        name="composer_detail",
    ),
    path(
        "composers/create/",
        ComposerCreateView.as_view(),
        name="composer_create",
    ),
    path(
        "composers/<int:pk>/update/",
        ComposerUpdateView.as_view(),
        name="composer_update",
    ),
    path(
        "composers/<int:pk>/delete/",
        ComposerDeleteView.as_view(),
        name="composer_delete",
    ),
    # Arranger URLs
    path("arrangers/", ArrangerListView.as_view(), name="arrangers_list"),
    path(
        "arrangers/<int:pk>/",
        ArrangerDetailView.as_view(),
        name="arranger_detail",
    ),
    path(
        "arrangers/create/",
        ArrangerCreateView.as_view(),
        name="arranger_create",
    ),
    path(
        "arrangers/<int:pk>/update/",
        ArrangerUpdateView.as_view(),
        name="arranger_update",
    ),
    path(
        "arrangers/<int:pk>/delete/",
        ArrangerDeleteView.as_view(),
        name="arranger_delete",
    ),
    # Genre views
    path("genres/", GenreListView.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("genres/create/", GenreCreateView.as_view(), name="genre_create"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre_update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre_delete"),
    # Publisher views
    path("publishers/", PublisherListView.as_view(), name="publishers_list"),
    path(
        "publishers/<int:pk>/", PublisherDetailView.as_view(), name="publisher_detail"
    ),
    path("publishers/create/", PublisherCreateView.as_view(), name="publisher_create"),
    path(
        "publishers/<int:pk>/update/",
        PublisherUpdateView.as_view(),
        name="publisher_update",
    ),
    path(
        "publishers/<int:pk>/delete/",
        PublisherDeleteView.as_view(),
        name="publisher_delete",
    ),
    # LendingOrganizations views
    path(
        "lendingorganizations/",
        LendingOrganizationListView.as_view(),
        name="lendingorganizations_list",
    ),
    path(
        "lendingorganizations/<int:pk>/",
        LendingOrganizationDetailView.as_view(),
        name="lendingorganization_detail",
    ),
    path(
        "lendingorganizations/create/",
        LendingOrganizationCreateView.as_view(),
        name="lendingorganization_create",
    ),
    path(
        "lendingorganizations/<int:pk>/update/",
        LendingOrganizationUpdateView.as_view(),
        name="lendingorganization_update",
    ),
    path(
        "lendingorganizations/<int:pk>/delete/",
        LendingOrganizationDeleteView.as_view(),
        name="lendingorganization_delete",
    ),
    # BorrowingOrganizations views
    path(
        "borrowingorganizations/",
        BorrowingOrganizationListView.as_view(),
        name="borrowingorganizations_list",
    ),
    path(
        "borrowingorganizations/<int:pk>/",
        BorrowingOrganizationDetailView.as_view(),
        name="borrowingorganization_detail",
    ),
    path(
        "borrowingorganizations/create/",
        BorrowingOrganizationCreateView.as_view(),
        name="borrowingorganization_create",
    ),
    path(
        "borrowingorganizations/<int:pk>/update/",
        BorrowingOrganizationUpdateView.as_view(),
        name="borrowingorganization_update",
    ),
    path(
        "borrowingorganizations/<int:pk>/delete/",
        BorrowingOrganizationDeleteView.as_view(),
        name="borrowingorganization_delete",
    ),
    # RentingOrganizations views
    path(
        "rentingorganizations/",
        RentingOrganizationListView.as_view(),
        name="rentingorganizations_list",
    ),
    path(
        "rentingorganizations/<int:pk>/",
        RentingOrganizationDetailView.as_view(),
        name="rentingorganization_detail",
    ),
    path(
        "rentingorganizations/create/",
        RentingOrganizationCreateView.as_view(),
        name="rentingorganization_create",
    ),
    path(
        "rentingorganizations/<int:pk>/update/",
        RentingOrganizationUpdateView.as_view(),
        name="rentingorganization_update",
    ),
    path(
        "rentingorganizations/<int:pk>/delete/",
        RentingOrganizationDeleteView.as_view(),
        name="rentingorganization_delete",
    ),
    # Music urls
    path(
        "music/",
        MusicListView.as_view(),
        name="music_list",
    ),
    path(
        "music/<int:pk>/",
        MusicDetailView.as_view(),
        name="music_detail",
    ),
    path(
        "music/create/",
        MusicCreateView.as_view(),
        name="music_create",
    ),
    path(
        "music/<int:pk>/update/",
        MusicUpdateView.as_view(),
        name="music_update",
    ),
    path(
        "music/<int:pk>/delete/",
        MusicDeleteView.as_view(),
        name="music_delete",
    ),
]
