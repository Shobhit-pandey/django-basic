# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect ,reverse
from accounts.form import RegistrationForm , EditProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    numbers=[1,2,3,4,5]
    name='Shobhit Pandey'
    args={'myName':name,'numbers':numbers}
    return render(request,'accounts/home.html',args)


@login_required
def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)



def about(request):
    return render(request,'accounts/about.html')

def contact(request):
    return render(request,'accounts/contact.html')



def register(request):
    if (request.method=='POST'):
        form=RegistrationForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request,'accounts/register.html',args)


@login_required
def edit_profile(request):
    if request.method=='POST':
        form=EditProfile(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form=EditProfile(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)