from django import forms
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(initial="Anywhere")
    country = forms.CharField(initial="New York")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(empty_label="Any kind", queryset=models.RoomType.objects.all())
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.IntegerField(required=False)
    amenities = forms.ModelMultipleChoiceField(queryset=models.Amenity.objects.all(),
                                               widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(queryset=models.Facility.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)
