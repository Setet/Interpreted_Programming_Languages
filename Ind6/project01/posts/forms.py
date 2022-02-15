from .models import Author, Gallery
from django import forms


class PictureForm(forms.Form):
    name = forms.CharField(label="Name")
    id_author = forms.ModelMultipleChoiceField(queryset=Author.author_obj.all())
    genre = forms.CharField(label="Genre")
    id_gallery = forms.ModelMultipleChoiceField(queryset=Gallery.gallery_obj.all())
    timestamp = forms.DateField(label="Timestamp", widget=forms.DateInput)


class AuthorForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    second_name = forms.CharField(label="Last Name")
    pseudonym = forms.CharField(label="Pseudonym")
    date_birth = forms.DateField(label="Date Birth", widget=forms.DateInput)


class GalleryForm(forms.Form):
    name = forms.CharField(label="Name")
    address = forms.CharField(label="Address")
