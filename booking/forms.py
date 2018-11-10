from django import forms
from .models import BookingListIndi, BookingListOrga

class PostForm1(forms.ModelForm):
    class Meta:
        model = BookingListIndi
        exclude = ('code', 'visited')

class PostForm2(forms.ModelForm):
    class Meta:
        model = BookingListOrga
        exclude = ('code', 'visited')
