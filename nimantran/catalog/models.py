from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Category(models.Model):
    """
    Model representing the category of an event i.e. Marriage, Birthday, Obituary etc.
    """
    name = models.CharField(max_length=200, help_text = "Enter an event cateory(e.g. Marriage, Birthday etc.)")

    def __str__(self):
        return self.name

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(help_text = "Person's phone number")
    dob = models.DateField(null = True, help_text = "Date of Birth")
    email = models.EmailField(help_text = "Email id")

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('people-detail', args = [str(self.id)])

class Venue(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500, help_text = "address of the venue")
    capacity = models.IntegerField(help_text = "Maximum capacity of the venue")

    def __str__(self):
        return self.name

class Event(models.Model):
    """
    Model representing the event
    """
    title = models.CharField(max_length = 200, help_text = "Provide a title to your event.")
    description = models.CharField(max_length = 500, help_text = "Briefly describe in 500 chars.")
    dateFrom = models.DateField()
    dateTo = models.DateField()
    organizer = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    cateory = models.ManyToManyField(Category, help_text = "Select a category for this event")
    venue = models.ForeignKey(Venue, help_text = "Select the venue", on_delete = models.DO_NOTHING)
    public = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    def display_category(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ cateory.name for category in self.cateory.all()[:3] ])

class Invitation(models.Model):
    """
    Model representing each invite
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "Unique ID for this invite")
    event = models.ForeignKey(Event, help_text = "select the event for this event", on_delete = models.DO_NOTHING)
    invitee = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    note = models.CharField(max_length = 1000, help_text = "A personalised note for the guest", null = True)

    INVITE_STATUS = (
        ('i', 'Interested'),
        ('g', 'Going'),
        ('n', 'Not going'),
    )

    status = models.CharField(max_length = 1, choices = INVITE_STATUS, default = 'n', help_text = 'Interest in the event')

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.event.title)

    def get_absolute_url(self):
        return reverse('invite-detail', args=[str(self.id)])
