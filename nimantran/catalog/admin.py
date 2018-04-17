from django.contrib import admin

# Register your models here.
from .models import Category, People, Event, Venue, Invitation

admin.site.register(Category)
admin.site.register(People)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Invitation)
