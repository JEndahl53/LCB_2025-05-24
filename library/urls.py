# library/urls.py
from django.urls import path

from common.views import HomePageView
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from library.views import (
    ComposerListView,
    ComposerDetailView,
    ComposerCreateView,
    ComposerUpdateView,
    ComposerDeleteView,
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
]
