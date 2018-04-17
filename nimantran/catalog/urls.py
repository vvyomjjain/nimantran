from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('events/', views.EventListView.as_view(), name='events'),
	path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('venue/<int:pk>', views.VenueDetailView.as_view(), name='venue-detail'),
    path('myinvits/', views.InvitedListView.as_view(), name='my-invited'),
    path('myinvits/<int:pk>', views.InvitedDetailView.as_view(), name='invite-detail'),
    path('myorganized/', views.OrganizedListView.as_view(), name='my-organized'),
]
