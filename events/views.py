from django.shortcuts import render,redirect
from datetime import datetime
from .models import Event,Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect

# adding events

def add_event(request):
    submitted=False
    if request.method=='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',
                  {'form':form,'submitted':submitted})



# updatng views
def update_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form= VenueForm(request.POST or None,instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html',
                  {'venue': venue,
                   'form': form})

# searching venues
def search_venue(request):
    if request.method=='POST':
        searched=request.POST['searched']
        venues=Venue.objects.filter(name__contains=searched)

        return render(request, 'events/search_venue.html',
                      {'venues': venues,
                       'searched': searched})
    else:
        return render(request, 'events/search_venue.html',
                      {})



# showing venue with clickable links
def show_venue(request,venue_id):
    venue=Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',
                  {'venue': venue})

#list venues
def list_venues(request):
    venue_list=Venue.objects.all()
    return render(request, 'events/venues.html',
                  {'venue_list': venue_list})
# venue
def add_venue(request):
    submitted=False
    if request.method=='POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/venue.html',
                  {'form':form,'submitted':submitted})


# Create your views here.
def home(request,year=datetime.now().year, month=datetime.now().strftime('%B')):
    name= 'john'
    return render(request, 'events/home.html',{
        'name':name,
        'year':year,
        'month':month

    })
def all_events(request):
    event_lists=Event.objects.all()
    return render(request,'events/event_list.html',
                  {'event_list':event_lists})



