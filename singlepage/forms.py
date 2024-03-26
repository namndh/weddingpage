from django import forms
from .models import Wish, RSVP


class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['author', 'wish']


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['name', 'num_guests', 'attendance', 'party']
        labels = {
            "name":  "Cho vợ chồng mình biết tên bạn nhé!",
            "num_guests": "Bạn đi mấy mình?",
            "attendance": "Chắc là tham dự rồi?",
            "party": "Bạn tham gia tiệc cưới nào?"
        }
