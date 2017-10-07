from django.shortcuts import render
from django.utils import timezone
import urllib


# Create your views here.
def index(request):
    return render(request, 'report/index.html')


def about(request):
    return render(request, 'report/info_aboutus.html')


def report_list(request):
    return render(request, 'report/report_list.html')


def report_wage(request):
    return render(request, 'report/report_minimum_wage.html')


def report_sexual(request):
    return render(request, 'report/report_sexual.html')


def report_sexual_case1(request):
    attacker = urllib.parse.unquote(request.COOKIES.get('attacker'));
    return render(request, 'report/report_sexual_case1.html',{'attacker': attacker})


def report_sexual_case2(request):
    attacker = urllib.parse.unquote(request.COOKIES.get('attacker'));
    return render(request, 'report/report_sexual_case2.html',{'attacker': attacker})
