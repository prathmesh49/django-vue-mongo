from django import forms

class AddDish(forms.Form):
    name = forms.CharField(label="dish name", max_length=100)
    price = forms.DecimalField(label="dish price",max_digits=10, decimal_places=2)
    availability = forms.BooleanField(label="dish available",initial=True, required=False)