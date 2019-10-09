"""mail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from data import views
from user import views as user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$^',views.home),


    url(r'^saveuser/',user.saveuser,name='saveuser'),
    url(r'^saveuserdetails/',user.saveuserdetails,name='saveuserdetails'),
    url(r'^getstate/',user.getstate,name='getstate'),
    url(r'^getdistrict/',user.getdistrict,name='getdistrict'),
    url(r'^validate_username/',user.validate_username,name='validate_username'),
    url(r'^logout/',user.logout_request,name='logout'),
    url(r'^register/',user.register,name='register'),
    url(r'^userlogin/',user.userlogin,name='userlogin'),

    url(r'^forgot/',user.forgot,name='forgot'),
    url(r'^changeforgotpas/',user.changeforgotpas,name='changeforgotpas'),
    url(r'^setnewpass/',user.setnewpass,name='setnewpass'),
    url(r'^composemail/',user.composemail,name='composemail'),
    url(r'^sendmail/',user.sendmail,name='sendmail'),
    url(r'^resivemail/',user.inbox,name='inbox'),
    url(r'^viewmessage/(?P<msg_id>\d+)/$',user.viewmessage,name='viewmessage'),
    url(r'^savemail/',user.savemail,name='savemail'),
    url(r'^savedmails/',user.savedmails,name='savedmails'),
    url(r'^spam/',user.spam,name='spam'),

    url(r'^addcontact/',user.addcontact,name='addcontact'),
    url(r'^savecontact/',user.savecontact,name='savecontact'),
    url(r'^userhome/',user.inbox,name='userhome'),
    url(r'^enlargefile/(?P<msg_id>\d+)/$',user.enlargefile,name='enlargefile'),
    url(r'^forward/(?P<msg_id>\d+)/$',user.forward,name='forward'),
##    url(r'^forward/',user.forward,name='forward'),
    url(r'^profile/',user.profile,name='profile'),
    url(r'^nex/',user.nex,name='nex'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
