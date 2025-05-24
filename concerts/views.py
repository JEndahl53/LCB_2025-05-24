# concerts/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    View for the home page.
    """

    template_name = "home.html"
