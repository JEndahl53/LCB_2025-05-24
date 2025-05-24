from django.contrib import admin
from .models import Concert, Conductor, Guest, Venue


# Register your models here.
admin.site.register(Concert)
admin.site.register(Conductor)
admin.site.register(Guest)
admin.site.register(Venue)
