# library/urls.py
from django.urls import path

from common.views import HomePageView
from django.urls import reverse_lazy

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
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Composer URLs
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
]
