"""lmsweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views,user_login
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('app.urls')),
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('404/', views.page_not_found, name='404'),
    path('courses/filter-data',views.filter_data, name="filter-data"),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('search/', views.search_course, name='search'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/register/', user_login.REGISTER, name='register'),
    path('dologin/', user_login.do_login, name='dologin'),
    path('accounts/profile/', user_login.PROFILE, name='profile'), 
    path('accounts/profile/update', user_login.Profile_Update, name='profile_update'), 
    path('checkout/<slug:slug>/', views.checkout, name='checkout'),
    path('my-course/', views.my_course, name='my_course'),
    path('verify-payment', views.verify_payment, name='verify_payment'),
    path('course/watch-course/<slug:slug>/', views.watch_course, name='watch_course'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
