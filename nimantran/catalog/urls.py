from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import uuid
from django.conf.urls import url
from . import views as core_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('events/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue-detail'),

    path('myinvits/', views.InvitedListView.as_view(), name='my-invited'),
    path('myinvits/<uuid:pk>', views.InvitedDetailView.as_view(), name='invite-detail'),
    path('myorganized/', views.OrganizedListView.as_view(), name='my-organized'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='profile'),

    path('events/create/', views.EventCreate.as_view(), name = 'events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='events_delete'),

    path('invitations/create/', views.InviteCreate.as_view(), name='invite_create'),
    path('invitations/<uuid:pk>/update/', views.InviteUpdate.as_view(), name='invite_update'),
    url(r'^signup/$', core_views.signup, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
