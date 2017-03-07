from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from shark import models
import json


# Create your views here.

def acc_login(request):
    '''
    登录,如果没有登录就先登录
    :param request:
    :return:
    '''
    print(request.POST)
    if request.method == 'POST':

        user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password')
        )
        if user is not None:
            print(login(request, user))
            return HttpResponse('That is ok')
        else:
            login_err = "wrong username or password!"
            return render(request, 'login.html', {'login_err': login_err})
    else:
        return render(request, 'shark/login.html')
        # return HttpResponse('ERROR !!!')


def acc_logout(request):
    '''
    退出,返回到首页
    :param request:
    :return:
    '''
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


@login_required()
def index(request):
    '''
    Dashboard
    :param request:
    :return:
    '''
    host_obj = models.Asset.objects.all()
    host_objs = models.Asset.objects

    dic_count = {'on_count': host_objs.filter(status='0').count(),
                 'off_count': host_objs.filter(status='1').count(),
                 'unKnow_count': host_objs.filter(status='2').count(),
                 'fail_count': host_objs.filter(status='3').count(),
                 'bak_count': host_objs.filter(status='4').count(),
                 }
    idc_obj = models.IDC.objects.all()


    on = host_obj.filter(status='0').filter(idc_id=2).count()
    # print(on)
    idc_dic = {}
    idc_list = []

    idc_dic ={
        'bejing':{'on':1,'off':2},
    }
    for i in models.IDC.objects.all():
        # idc_list.append(i.i)
        host_obj.filter(status='0').filter(idc_id=i.id).count()


    # linux_count = host_objs.filter(os='linux').count()
    # ubuntu_count = host_objs.filter(os='ubuntu').count()
    # win_count = host_objs.filter(os='windows 7').count()
    return render(request, 'shark/index.html', {'host': host_obj,
                                                'dic_count': dic_count,
                                                'idc':idc_obj

                                                # 'linux_count':linux_count,
                                                # 'ubuntu_count':ubuntu_count,
                                                # 'win_count':win_count,
                                                })
