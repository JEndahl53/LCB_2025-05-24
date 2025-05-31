# library/filters.py
# uses django-filters for search functionality

import django_filters
from django.db.models import Q
from .models import Music, Genre

# don't need Composer or Arranger, as those come from the Music model


class MusicFilter(django_filters.FilterSet):
    # Live search across multiple fields
    search = django_filters.CharFilter(
        method="filter_search",
        label="Search",
        widget=django_filters.widgets.forms.TextInput(
            attrs={
                "placeholder": "Search titles, composers, arrangers...",
                "class": "w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent",
                "id": "live-search",
            }
        ),
    )

    # Difficulty dropdown
    difficulty = django_filters.ChoiceFilter(
        choices=[("", "All Difficulties")] + Music.DIFFICULTY_CHOICES,
        empty_label=None,
        widget=django_filters.widgets.forms.Select(
            attrs={
                "class": "px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent",
            }
        ),
    )

    # Status dropdown
    status = django_filters.ChoiceFilter(
        choices=[("", "All Status")] + Music.STATUS_CHOICES,
        empty_label=None,
        widget=django_filters.widgets.forms.Select(
            attrs={
                "class": "px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
    )

    # Genre multi-select
    genre = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        widget=django_filters.widgets.forms.CheckboxSelectMultiple(
            attrs={"class": "genre-checkbox"}
        ),
    )

    class Meta:
        model = Music
        fields = ["search", "difficulty", "status", "genre"]

    def filter_search(self, queryset, name, value):
        """
        Custom search method that searches across title, composer names and arranger names.
        Uses Q objects for complex OR queries.
        """
        if value:
            return queryset.filter(
                Q(title__icontains=value)
                | Q(composer__first_name__icontains=value)
                | Q(composer__last_name__icontains=value)
                | Q(arranger__first_name__icontains=value)
                | Q(arranger__last_name__icontains=value)
            ).distinct()
        return queryset
