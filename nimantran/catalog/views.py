from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.
from .models import People, Venue, Event, Invitation

def index(request):
    """
    View function for homepage
    """
    # generating counts of the some main objects
    num_people = User.objects.all().count()
    num_venue = Venue.objects.all().count()
    num_event = Event.objects.all().count()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # render the html template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_people':num_people, 'num_venue':num_venue, 'num_event':num_event, 'num_visits':num_visits},
    )
from django.views import generic

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

class VenueDetailView(generic.DetailView):
    model = Venue

class InvitedListView(LoginRequiredMixin, generic.ListView):
    model = Invitation
    template_name = 'catalog/invited_list_user.html'

    def get_queryset(self):
        return Invitation.objects.filter(invitee=self.request.user)

class InvitedDetailView(LoginRequiredMixin, generic.DetailView):
    model = Invitation

class OrganizedListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'catalog/organized_list_user.html'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class UserDetailView(generic.DetailView):
    model = User
