"""ofgirlskorea URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
# from django.conf.urls.static import static

import report.views
import bamboo.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', report.views.index, name='report_main'),
    url(r'^about/$', report.views.about, name='info_about'),
    url(r'^about/ofgirlskorea$', report.views.aboutus, name='info_aboutus'),
    url(r'^howtouse/$', report.views.howto, name='info_howto'),
    url(r'^report/$', report.views.report_list, name='report_list'),
    url(r'^report/sexual/$', report.views.report_sexual, name='report_sexual'),
    url(r'^report/sexual/case1$', report.views.report_sexual_case1, name='report_sexual_case1'),
    url(r'^report/sexual/case2$', report.views.report_sexual_case2, name='report_sexual_case2'),
    url(r'^report/wage/$', report.views.report_wage, name='report_wage'),
    url(r'^report/etc/$', report.views.report_etc, name='report_etc'),
    url(r'^report/result/$', report.views.report_result, name='report_result'),
    url(r'^bamboo/$', bamboo.views.post_list, name='post_list'),
    # url(r'^bamboo/(?P<slug>[-\w]+)/$', bamboo.views.post_list_by_tag, name='post_list_by_tag'),
    url(r'^bamboo/category/(?P<pk>\d+)/$', bamboo.views.post_list_by_tag, name='post_list_by_tag'),
    url(r'^bamboo/(?P<pk>\d+)/$', bamboo.views.post_detail, name='post_detail'),
    url(r'^bamboo/new/$', bamboo.views.post_new, name='post_new'),
    url(r'^bamboo/(?P<pk>\d+)/edit/$', bamboo.views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', bamboo.views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', bamboo.views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^bamboo/(?P<pk>\d+)/edit/check/$', bamboo.views.post_edit_check_password, name='edit_check'),
    url(r'^bamboo/(?P<pk>\d+)/remove/check/$', bamboo.views.post_remove_check_password, name='remove_check'),
]
'''
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
