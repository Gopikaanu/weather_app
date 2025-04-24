from django import forms

class City(forms.Form):

    city = forms.CharField(max_length=100 ,label="enter city")

    