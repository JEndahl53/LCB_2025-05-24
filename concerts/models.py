# concerts/models.py
#
from django.db import models
from django.urls import reverse
from library.models import Music


import common.models


def construct_full_name(self):
    """
    Helper function to construct full name from first name, middle initial, and last name.
    """
    full_name = ""
    if self.title:
        full_name += self.title + " "
    if self.first_name:
        full_name += self.first_name + " "
    if self.middle_initial:
        full_name += self.middle_initial + " "
    full_name += self.last_name
    return full_name


class Venue(models.Model):
    """
    Model representing a concert venue.
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # Function to get output City, State ZIP
    def get_address2(self):
        parts = []
        if self.city:
            parts.append(self.city)

        state_zip_part = ""
        if self.state:
            state_zip_part += self.state
        if self.zip_code:
            state_zip_part += f" {self.zip_code}" if state_zip_part else self.zip_code

        if state_zip_part:
            parts.append(state_zip_part)

        return ", ".join(parts)


class Conductor(common.models.PersonBase):
    """
    Model representing a conductor.
    """

    title = models.CharField(max_length=10, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductors"

    def __str__(self):
        return construct_full_name(self)

    def get_absolute_url(self):
        return reverse("conductor_detail", args=[str(self.id)])


class Guest(common.models.PersonBase):
    """
    Model representing a guest.
    """

    title = models.CharField(max_length=10, blank=True, null=True)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"

    def __str__(self):
        return construct_full_name(self)

    def get_absolute_url(self):
        return reverse("guest_detail", args=[str(self.id)])


class Concert(models.Model):
    """
    Model representing a concert.
    """

    title = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    conductor = models.ManyToManyField(Conductor, blank=True)
    guest = models.ManyToManyField(Guest, blank=True)
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    music = models.ManyToManyField(
        Music,
        through="ConcertProgram",
        related_name="concerts",
        through_fields=("concert", "music"),
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("concert_detail", args=[str(self.id)])


# Now create the linking file


class ConcertProgram(models.Model):
    """
    Model representing the many-to-many relationship between Concert and Music.
    """

    concert = models.ForeignKey(
        Concert, on_delete=models.CASCADE, related_name="program_items"
    )
    music = models.ForeignKey(
        Music, on_delete=models.CASCADE, related_name="performances"
    )
    performance_order = models.PositiveIntegerField(
        default=0, help_text="Concert program order."
    )
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.concert.title} - {self.performance_order} - {self.music.title}"

    class Meta:
        # Ensure that the same music piece is not added to the same concert multiple times
        unique_together = [["concert", "performance_order"], ["concert", "music"]]
        ordering = ["concert", "performance_order"]
        verbose_name = "Concert Program Item"
        verbose_name_plural = "Concert Program Items"
