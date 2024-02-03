from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Borrow1
import random
from django.core.mail import send_mail
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.conf import settings
import mimetypes
import os
from wsgiref.util import FileWrapper
import zlib
import base64
import time


def begin(request):
    return render(request, 'page1.html')


def new(request):
    return render(request, 'loginpage.html')

def forgot(request):
    return render(request, 'forgot.html')

def change_pwd(request):
    myuser = User.objects.create_user(username, email_id, password)
    myuser.save()
    return render(request, 'change_pwd.html')


def for_to_otp(request):
    if request.method == 'POST':
        email_id = request.POST['email']
        check_user = User.objects.filter(email=email_id).first()
        if check_user:
            otp = str(random.randint(1000, 9999))
            subject = 'OTP Verification'
            message = f'Your OTP for GDriveX is: {otp}'
            from_email = settings.EMAIL_HOST
            recipient_list = [email_id]
            send_mail(subject, message, from_email, recipient_list)
            request.session['otp'] = otp
            messages.success(request, "Your account has been successfully created")
            return redirect('otp2_')

        else:
            messages.error(request, "User doesnot exist")
            return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_id = request.POST['email']
        password = request.POST['pwd']
        confirmpassword = request.POST['confpwd']
        phone = request.POST['phone']

        check_user = User.objects.filter(email=email_id).first()

        if check_user:
            messages.error(request, "User already exist")
            return redirect('home')

#     Check the signup requirements
        if len(username) > 20 or len(username) < 8:
            messages.error(request, "Username must be under 20 characters and atleast 8 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        if len(password) > 40 or len(password) < 8:
            messages.error(request, "Password must be under 40 characters and atleast 8 characters")
            return redirect('home')

        symbols = ['!', '@', '#', '$', '&', '*']
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        letters = list(password)

        if not str(phone).isdigit() :
            messages.error(request, "Phone number should only contain numbers")
            return redirect('home')

        if len(str(phone)) != 10:
            messages.error(request, "Phone number should only 10 digits")
            return redirect('home')

        if letters[0].isupper() is False:
            messages.error(request, "The First Letter of the password must be a capital letter")
            return redirect('home')

        sym = list(set(symbols).intersection(letters))
        num = list(set(numbers).intersection(letters))

        if sym == None:
            messages.error(request, "Password must contain alteast one of the following symbols: '!', '@', '#', '$', '&', '*'")
            return redirect('home')

        if num == None:
            messages.error(request,"Password must contain alteast one digit")
            return redirect('home')

        if password != confirmpassword:
            messages.error(request, "The 2 passwords must be same")
            return redirect('home')

        myuser = User.objects.create_user(username, email_id, password)
        myuser.save()
        otp = str(random.randint(1000, 9999))
        subject = 'OTP Verification'
        message = f'Your OTP for GDriveX is: {otp}'
        from_email = settings.EMAIL_HOST
        recipient_list = [email_id]
        send_mail(subject, message, from_email, recipient_list)

        request.session['otp'] = otp
        # request.session['username'] = username
        messages.success(request, "Your account has been successfully created")
        return redirect('otp1_')
    else:
        return HttpResponse('404 - Not Found')


def login_(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['pwd']

        user = authenticate(username=user_id, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('afterlogin')
        else:
            messages.error(request, "Invalid Credentials, Please try again Or If you don't have an please click sign in button to create an account")
            return redirect('home')

    else:
        return HttpResponse('404 - Not Found')

def logout_(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')


def otp1_(request):
    otp = request.session['otp']
    context = {'otp': otp}

    if request.method == 'POST':
        otp1= request.POST.get('otp1')
        otp2= request.POST.get('otp2')
        otp3= request.POST.get('otp3')
        otp4= request.POST.get('otp4')
        __otp__ = str(otp1 + otp2 +otp3 +otp4)

        print(otp)
        print(__otp__)

        if otp == __otp__:
                return redirect('afterlogin')
        else:
            print('Wrong OTP')
            context = {'message': 'Wrong OTP', 'class': 'danger', 'otp': otp}
            return render(request, 'otp.html', context)
    return render(request, 'otp.html', context)

def otp2_(request):
    otp = request.session['otp']
    context = {'otp': otp}

    if request.method == 'POST':
        otp1= request.POST.get('otp1')
        otp2= request.POST.get('otp2')
        otp3= request.POST.get('otp3')
        otp4= request.POST.get('otp4')
        __otp__ = str(otp1 + otp2 +otp3 +otp4)

        print(otp)
        print(__otp__)

        if otp == __otp__:
                return redirect('change_pwd')
        else:
            print('Wrong OTP')
            context = {'message': 'Wrong OTP', 'class': 'danger', 'otp': otp}
            return render(request, 'otp.html', context)
    return render(request, 'otp.html', context)


def afterlogin(request):
    return render(request, 'equipmhome.html')

def sports(request):
    return render(request, 'sportslist6fig.html')

def itemlist1(request):
    return render(request, 'item-list1.html')

def itemlist2(request):
    return render(request, 'item-list2.html')

def itemlist3(request):
    return render(request, 'item-list3.html')
def itemlist4(request):
    return render(request, 'item-list4.html')
def itemlist5(request):
    return render(request, 'item-list5.html')
def itemlist6(request):
    return render(request, 'item-list6.html')


def button_action(request):
    if request.method == 'POST':
        button_value = request.POST.get('button', None)

        if button_value == 'bat':
            return render(request, 'lastpage.html')

        elif button_value == 'ball':
            return render(request, 'lastpage.html')



# def borrowrecord(request):
#     if request.method == "POST":
#         inputText = request.POST.get('inputText')
#         dateTime1 = request.POST.get('dateTime1')
#         dateTime2 = request.POST.get('dateTime2')
#         #
#         en = BorrowRecord(inputText=inputText)
#         en.save()
#         return render(request, "lastpage.html")


def borrow(request):
    if request.method == "POST":
        inputText = request.POST.get('inputText')
        hi = Borrow1(inputText=inputText)
        hi.save()
        return render(request, "lastpage.html")
