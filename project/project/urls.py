"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('userindex',views.userindex,name='userindex'),
    path('companyindex',views.companyindex,name='companyindex'),
    path('logins',views.logins),
    path('logout',views.logout,name='logout'),
    path('userregistration',views.userregistration),
    path('companyregistration',views.companyregistration),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userprofileedit',views.userprofileedit),
    path('updat/<int:id>',views.updat, name='updat'),
    path('updat/updates/<int:id>',views.updates, name='updates'),
    path('companyprofile',views.companyprofile,name='companyprofile'),
    path('companyprofileedit',views.companyprofileedit),
    path('companyupdat/<int:id>',views.companyupdat, name='companyupdat'),
    path('companyupdat/companyupdates/<int:id>',views.companyupdates, name='companyupdates'),
    path('addjob',views.addjob, name='addjob'),
    path('jobview',views.jobview,name='jobview'),
    path('search',views.search),
    path('managejob',views.managejob,name='managejob'),
    path('application',views.applications,name='application'),
    path('appliedjobs',views.appliedjobs,name='appliedjobs'),
    path('editjob/<int:id>',views.editjob, name='editjob'),
    path('deletejob/<int:id>/', views.deletejob, name='deletejob'),
    path('viewapplication',views.viewapplication,name='viewapplication'),
    path('applicationaccept/<int:id>/', views.applicationaccept, name='applicationaccept'),
    path('notifications',views.notifications,name='notifications'),
    path('notificationcom',views.notificationcom,name='notificationcom'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

