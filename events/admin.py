from django.contrib import admin

# Register your models here.

from .models import Venue
from .models import Myhoteluser
from .models import Event

# admin.site.register(Venue)
admin.site.register(Myhoteluser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display=('name','address','phone')
    ordering=('name',)
    search_fields=('name','phone')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=(('name','venue'),'event_date','description','managers')
    list_display=('name','event_date','venue')
    list_filter=('event_date','venue')
    ordering=('event_date',)