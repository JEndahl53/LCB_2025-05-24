# library/models.py

from django.db import models
from django.urls import reverse


class Composer(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_date} - {self.death_date})"

    def get_absolute_url(self):
        return reverse("composer_detail", args=[str(self.id)])

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_sort_name(self):
        if not {self.first_name}:
            return f"{self.last_name}"
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name = "Composer"
        verbose_name_plural = "Composers"
        ordering = ["last_name", "first_name"]


class Arranger(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.birth_date} - {self.death_date})"

    def get_absolute_url(self):
        return reverse("composer_detail", args=[str(self.id)])

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_sort_name(self):
        if not {self.first_name}:
            return f"{self.last_name}"
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        verbose_name = "Arranger"
        verbose_name_plural = "Arrangers"
        ordering = ["last_name", "first_name"]


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        ordering = ["name"]


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("publisher_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["name"]


class LoaningOrganization(models.Model):
    # Group that we loaned must to
    name = models.CharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("loaning_organization_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loaning Organization"
        verbose_name_plural = "Loaning Organizations"
        ordering = ["name"]


class BorrowingOrganization(models.Model):
    # Group that we borrow music from
    name = models.CharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("borrowing_organization_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Borrowing Organization"
        verbose_name_plural = "Borrowing Organizations"
        ordering = ["name"]


class RentingOrganization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("renting_organization_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Renting Organization"
        verbose_name_plural = "Renting Organizations"
        ordering = ["name"]


class Music(models.Model):

    DIFFICULTY_CHOICES = [
        ("", "Select Difficulty"),
        ("E", "Easy"),
        ("ME", "Moderately Easy"),
        ("M", "Moderate"),
        ("MD", "Moderately Difficult"),
        ("D", "Difficult"),
    ]
    STATUS_CHOICES = [
        ("", "Select Status"),
        ("O", "Owned"),
        ("L", "Loaned To"),
        ("R", "Rented"),
        ("B", "Borrowed From"),
        ("M", "Missing"),
    ]

    title = models.CharField(max_length=255)
    composer = models.ManyToManyField(Composer, related_name="compositions", blank=True)
    arranger = models.ManyToManyField(Arranger, blank=True, related_name="arrangements")
    location_drawer = models.CharField(max_length=5, blank=True, null=True)
    location_number = models.CharField(max_length=5, blank=True, null=True)
    genre = models.ManyToManyField(Genre, blank=True, related_name="genres")
    difficulty = models.CharField(
        max_length=2, choices=DIFFICULTY_CHOICES, blank=True, default=""
    )
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, blank=True, default=""
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_NULL, blank=True, null=True
    )
    year_published = models.IntegerField(blank=True, null=True)
    # Owned music pieces
    date_acquired = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    purchase_source = models.CharField(max_length=255, blank=True, null=True)
    # Loaned music pieces (loaned to)
    loaning_organization = models.ForeignKey(
        LoaningOrganization, on_delete=models.SET_NULL, blank=True, null=True
    )
    loan_start_date = models.DateField(blank=True, null=True)
    expected_return_date = models.DateField(blank=True, null=True)
    # Rented music pieces
    renting_organization = models.ForeignKey(
        RentingOrganization, on_delete=models.SET_NULL, blank=True, null=True
    )
    rental_start_date = models.DateField(blank=True, null=True)
    rental_end_date = models.DateField(blank=True, null=True)
    rental_fee = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=2
    )
    borrowing_organization = models.ForeignKey(
        BorrowingOrganization, on_delete=models.SET_NULL, blank=True, null=True
    )
    borrowing_start_date = models.DateField(blank=True, null=True)
    expected_borrowing_return_date = models.DateField(blank=True, null=True)
    # Miscellaneous
    duration = models.DurationField(blank=True, null=True)
    score_missing = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("music_piece_detail", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Music"
        verbose_name_plural = "Music"
        ordering = ["title"]
