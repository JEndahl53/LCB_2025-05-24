# core/views.py


from django.db.models import Count
from concerts.models import Concert, Venue
from library.models import Music, Composer, Genre
from common.models import PersonBase
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from common.forms import PersonBaseForm


class HomePageView(TemplateView):
    """
    View for the home page that displays statistic snd sections
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add statistics for both sections
        context["concert_count"] = Concert.objects.count()
        context["venue_count"] = Venue.objects.count()
        context["music_piece_count"] = Music.objects.count()
        context["composer_count"] = Composer.objects.count()
        context["genre_count"] = Genre.objects.count()

        # Example of additional data aggregation
        context["most_performed_piece"] = (
            Music.objects.annotate(num_performances=Count("concerts"))
            .order_by("-num_performances")
            .first()
        )
        context["most_performed_piece"] = (
            Music.objects.annotate(num_performances=Count("concerts"))
            .order_by("-num_performances")
            .first()
        )
        # context["most_performed_genre"] = (
        #     Genre.objects.annotate(num_performances=Count("music__concerts"))
        #     .order_by("-num_performances")
        #     .first()
        # )
        # context["most_performed_composer"] = (
        #     Composer.objects.annotate(num_performances=Count("music__concerts"))
        #     .order_by("-num_performances")
        #     .first()
        # )
        return context
