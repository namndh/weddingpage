from django import forms
from .models import Wish, RSVP


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['author', 'wish']


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'email', 'attendance', 'party']
        labels = {
            "name":  "Tên của bạn",
            "email": "Email",
            "attendance": "Xác nhận tham dự",
            "party": "Tiêc cưới sẽ tham dự"
        }
