from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(max_length=255)
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField()
