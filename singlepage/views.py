import json

from django.http import JsonResponse
from django.shortcuts import render

from .forms import WishForm, RSVPForm
from .models import Wish, RSVP


def index(request):
    if request.method == 'POST':
        form_name = request.POST.get('form_name')
        if form_name == "rsvp-form":
            form = RSVPForm(request.POST)
            if form.is_valid():
                rsvp = form.save()
                print(form)
                if rsvp.attendance == "Có":
                    return JsonResponse({'message': 1})
                else:
                    return JsonResponse({'message': 0})
        else:
            form = WishForm(request.POST)
            if form.is_valid():
                new_wish = form.save()
                wish_data = {
                    'id': new_wish.id,
                    'author': new_wish.author,
                    'wish': new_wish.wish,
                    'created_at': new_wish.created_at.strftime("%Y-%m-%d %H:%M:%S")
                }
                return JsonResponse(wish_data)

    form = WishForm()
    rsvp_form = RSVPForm()
    wishes = Wish.objects.all().order_by('created_at')  # Fetch existing wishes
    wishes_data = [
        {
            'id': wish.id,
            'author': wish.author,
            'wish': wish.wish,
            'created_at': wish.created_at.strftime("%Y-%m-%d %H:%M:%S")
        } for wish in wishes
    ]
    context = {'items': json.dumps(wishes_data), 'form': form, 'rsvp_form': rsvp_form}

    return render(request, 'singlepage/index.html', context)
