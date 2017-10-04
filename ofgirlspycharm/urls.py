"""ofgirlspycharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import report.views
import bamboo.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^report/$', report.views.report_list, name='report_list'),
    url(r'^report/wage/$', report.views.report_wage, name='report_wage'),
    url(r'^bamboo/$', bamboo.views.post_list, name='post_list'),
    url(r'^bamboo/(?P<pk>\d+)/$', bamboo.views.post_detail, name='post_detail'),
    url(r'^bamboo/new/$', bamboo.views.post_new, name='post_new'),
    url(r'^bamboo/(?P<pk>\d+)/edit/$', bamboo.views.post_edit, name='post_edit'),
]
