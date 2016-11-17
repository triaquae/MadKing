#_*_coding:utf-8_*_
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
import django

from assets.dashboard import AssetDashboard
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    return render(request,'index.html',)



def acc_login(request):
    if request.method == "POST":

        username = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.valid_end_time: #设置了end time
                if django.utils.timezone.now() > user.valid_begin_time and django.utils.timezone.now()  < user.valid_end_time:
                    auth.login(request,user)
                    request.session.set_expiry(60*30)
                    #print 'session expires at :',request.session.get_expiry_date()
                    return HttpResponseRedirect('/')
                else:
                    return render(request,'login.html',{'login_err': 'User account is expired,please contact your IT guy for this!'})
            elif django.utils.timezone.now() > user.valid_begin_time:
                    auth.login(request,user)
                    request.session.set_expiry(60*30)
                    return HttpResponseRedirect('/')

        else:
            return render(request,'login.html',{'login_err': 'Wrong username or password!'})
    else:
        return render(request, 'login.html')
