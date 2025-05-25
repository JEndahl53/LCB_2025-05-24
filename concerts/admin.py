from django.contrib import admin
from .models import Concert, Conductor, Guest, Venue, ConcertProgram

admin.site.register(Conductor)
admin.site.register(Guest)
admin.site.register(Venue)


class ConcertProgramInline(admin.TabularInline):
    """
    Inline admin interface for the ConcertProgram model.
    """

    model = ConcertProgram
    extra = 1


# Register your models here.
@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    """
    Admin interface for the Concert model.
    """

    inlines = [ConcertProgramInline]
    list_display = ("title", "date", "time", "venue")
    search_fields = ("title",)
    ordering = ("date",)
    list_per_page = 20


@admin.register(ConcertProgram)
class ConcertProgramAdmin(admin.ModelAdmin):
    """
    Admin interface for the ConcertProgram model.
    """

    list_display = ("concert", "music", "performance_order")
    list_filter = ["concert"]
    search_fields = ("concert__title", "music__title")
    ordering = ("concert", "performance_order")
    list_per_page = 20
