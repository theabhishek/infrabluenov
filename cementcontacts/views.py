from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contactcement
from django.core.mail import send_mail
from django.contrib.auth.models import User


def cementinquiry(request):
    if request.method == 'POST':
        cement_id = request.POST['cement_id']
        cement_title = request.POST['cement_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contactcement.objects.all().filter(cement_id=cement_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry . Please wait until we get back to you.')
                return redirect('/cements/'+cement_id)

        contactcement = Contactcement(cement_id=cement_id, cement_title=cement_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        state=state, email=email, phone=phone, message=message)



        contactcement.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cements/'+cement_id)
