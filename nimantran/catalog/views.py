from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import People, Venue, Event, Invitation
from .forms import SelectResponse

from django.views import generic

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

def about(request):
    """
    View function for about page
    """

    return render(
        request,
        'about.html',
    )

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

def change_status(request, pk):
    invite = get_object_or_404(Invitation, pk=pk)

    if request.method == 'POST':
        form = SelectResponse(request.POST)
        if form.is_valid():
            invite.status = form.cleaned_data['new_status']
            invite.save()

            return HttpResponseRedirect(reverse('invite-detail') )
    else:
        form = SelectResponse()

    return render(request, 'catalog/myinvits/<uuid:pk>/', {'form': form, 'invite': invite})

class VenueDetailView(generic.DetailView):
    model = Venue

class InvitedListView(LoginRequiredMixin, generic.ListView):
    model = Invitation
    template_name = 'catalog/invited_list_user.html'

    def get_queryset(self):
        return Invitation.objects.filter(invitee=self.request.user)

class InvitedDetailView(LoginRequiredMixin, generic.DetailView):
    model = Invitation
    template_name = 'catalog/invitation_detail.html'

class OrganizedListView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'catalog/organized_list_user.html'

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_going')
@permission_required('catalog.can_edit')
def my_view(request):

    from django.contrib.auth.mixins import PermissionRequiredMixin

    class MyView(PermissionRequiredMixin, View):
        permission_required = 'catalog.can_mark_going'
        # Or multiple permissions
        permission_required = ('catalog.can_mark_going', 'catalog.can_edit')
        # Note that 'catalog.can_edit' is just an example
        # the catalog application doesn't have such permission!


class UserDetailView(generic.DetailView):
    model = User

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'catalog/user_detail.html'

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')

class InviteUpdate(LoginRequiredMixin, UpdateView):
    model = Invitation
    fields = ['status']

class InviteCreate(LoginRequiredMixin, CreateView):
    model = Invitation
    fields = ['event', 'invitee', 'note']

class InvitationCreate(LoginRequiredMixin, CreateView):
    model = Invitation
    fields = ['event', 'invitee', 'note']
