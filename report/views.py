from django.shortcuts import render
from django.utils import timezone

from .models import Report


# Create your views here.
def report_list(request):
    # reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    reports = Report.objects.all()
    return render(request, 'report/report_list.html', {'reports': reports})


def report_wage(request):
    return render(request, 'report/report_minimum_wage.html')