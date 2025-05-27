# core/models.py
from django.db import models


# PersonType holds the type of person, such as "conductor", "composer", etc.
class PersonType(models.Model):

    COMPOSER = "composer"
    CONDUCTOR = "conductor"
    ARRANGER = "arranger"
    GUEST = "guest"
    PERSON_TYPE_CHOICES = [
        (COMPOSER, "Composer"),
        (CONDUCTOR, "Conductor"),
        (ARRANGER, "Arranger"),
        (GUEST, "Guest"),
    ]

    name = models.CharField(max_length=15, unique=True, choices=PERSON_TYPE_CHOICES)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.get_name_display()


class PersonBase(models.Model):
    """
    Base model for all person-related models.
    """

    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    types = models.ManyToManyField(
        PersonType, blank=True, related_name="%(app_label)s_%(class)s_related"
    )
    # Conductor specific fields
    title = models.CharField(max_length=10, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    # Composer/Arranger specific fields
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    # Common fields
    comment = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["last_name", "first_name"]

    def get_full_name(self):
        """
        Returns the full name of the person.
        """
        if self.types.filter(name="conductor").exists():
            parts = [self.title, self.first_name, self.middle_initial, self.last_name]
            return " ".join(filter(None, parts))
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
