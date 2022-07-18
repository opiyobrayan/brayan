from django import forms
from django.forms import ModelForm
from .models import Venue,Event


# create venue form

class VenueForm(ModelForm):
    class Meta:

        model = Venue
        fields=('name','address','zip_code','phone','web','email_address')

       # doing style

        list_filter = ('name', 'address')
        labels={
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': ''
        }
        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Venue name'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
            'email_address':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'})

        }

  # event form

'name','wvent_date','venue','managers','descriptio','attendees'

class EventForm(ModelForm):
    class Meta:

        model = Event
        fields=('name','event_date','venue',
                'managers','description','attendees'
)

       # doing style

        list_filter = ('name', 'address')
        labels={
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'venue': 'venue',
            'managers': 'manager',
            'description': 'description',
            'attendees': 'Attendees'
        }
        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Event Name'}),
            'event_date':forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
            'managers':forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-select','placeholder':'Attendees'})

        }