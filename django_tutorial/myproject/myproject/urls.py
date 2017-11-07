"""myproject URL Configuration

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

# DEGISIKLIK, 1 ln
# boards klasorundeski views dosyasinin yukle
from boards import views

urlpatterns = [
    # DEGISIKLIK, 3 ln
    # BU BIR LIST, BU YUZDEN VIRGUL KOYMAYI UNUTMA!!!!
    # REGEX formatinda yaziyoruz URL'leri.
    # burada site uzantilarinin nasil olacagini ve nereden 
    # cagiralacaklarini belirtiyoruz. boards klasorundeski views dosyasinin
    # icindeki ilgili fonksyionlari cagiriyoruz.
    url(r'^$', views.home, name='home'),
    # Below is a dynamic URL, pk stands for Primary Key
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # we have to define '/about/' URL, we have to do it before
    # the username URL pattern to avoid any conflict with usernames
    # like 'about'.
    # url(r'^about/$', views.about, name='about'),
    # url(r'^about/author/$', views.about_author, name='about_author'),
    # url(r'^about/author/mayk/$', views.about_mayk, name='about_mayk'),
    url(r'^admin/', admin.site.urls),
]
