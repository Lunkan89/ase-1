from django.shortcuts import render
from django.http import HttpResponse
from .models import BookingListIndi, BookingListOrga
from .forms import PostForm1, PostForm2

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

import random
import string

def rand_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.

def index(request):
    return render(request, 'booking/index.html')

def book_indi(request):
    form = PostForm1()
    return render(request, 'booking/book_indi.html', {'form': form})

def book_orga(request):
    form = PostForm2()
    return render(request, 'booking/book_orga.html', {'form': form})

def con_indi(request):
    if request.method == 'POST':
        form = PostForm1(request.POST)
        if form.is_valid():
            name_person = form.cleaned_data['name_person']
            industry_name = form.cleaned_data['industry_name']
            date_visit = form.cleaned_data['date_visit']
            slots_present = form.cleaned_data['slots_present']
            visiting_members = form.cleaned_data['visiting_members']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            p = BookingListIndi(name_person=name_person, industry_name=industry_name, date_visit=date_visit,
                                slots_present=slots_present, visiting_members=visiting_members, street_name=street_name,
                                city_name=city_name, pin_code=pin_code, code=code)
            p.save()

            user = form.save(commit=False)
            user.is_active = False
            current_site = get_current_site(request)
            mail_subject = 'Here is your e-Ticket'
            message = render_to_string('booking/ticket_gen_indi.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'code': code,
            })
            to_email = 'lushaankkancherla1999@gmail.com'
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()

            return render(request, 'booking/success.html')
        else:
            return HttpResponse("<h3>Please Enter Valid Data</h3>")
    else:
        form = PostForm1()
    return render(request, 'booking/book_indi.html', {'form': form})

def con_orga(request):
    if request.method == 'POST':
        form = PostForm2(request.POST)
        if form.is_valid():
            name_person = form.cleaned_data['name_person']
            industry_name = form.cleaned_data['industry_name']
            organisation_name = form.cleaned_data['organisation_name']
            date_visit = form.cleaned_data['date_visit']
            slots_present = form.cleaned_data['slots_present']
            street_name = form.cleaned_data['street_name']
            city_name = form.cleaned_data['city_name']
            pin_code = form.cleaned_data['pin_code']
            code = rand_str()
            p = BookingListIndi(name_person=name_person, industry_name=industry_name,
                                organisation_name=organisation_name, date_visit=date_visit, slots_present=slots_present,
                                street_name=street_name, city_name=city_name, pin_code=pin_code, code=code)
            p.save()

            user = form.save(commit=False)
            user.is_active = False
            current_site = get_current_site(request)
            mail_subject = 'Here is your e-Ticket'
            message = render_to_string('booking/ticket_gen_indi.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'code': code,
            })
            to_email = 'lushaankkancherla1999@gmail.com'
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()

            return render(request, 'booking/success.html')
        else:
            return HttpResponse("<h3>Please Enter Valid Data</h3>")
    else:
        form = PostForm2()
    return render(request, 'booking/book_orga.html', {'form': form})

def list_indi(request):
    all_lists = BookingListIndi.objects.all()
    return render(request, 'booking/list_indi.html', {'all_lists':all_lists})

def list_orga(request):
    all_lists = BookingListOrga.objects.all()
    return render(request, 'booking/list_orga.html', {'all_lists':all_lists})

'''
def edit_indi(request, iden):
    return HttpResponse("<h3>Hold your Horses and Wait!</h3>")

def del_indi(request, iden):
    BookingListIndi.objects.get(pk=iden).delete()

def edit_orga(request, iden):
    return HttpResponse("<h3>Hold your Horses and Wait!</h3>")

def del_orga(request, iden):
    BookingListOrga.objects.get(pk=iden).delete()
'''