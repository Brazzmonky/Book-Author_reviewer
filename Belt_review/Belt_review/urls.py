"""Belt_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Belt_review_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('newUser',views.newUser),
    path('login',views.login),
    path('Success',views.Success),
    path('logout',views.logout),
    path('add_book_and_review',views.add_book_and_review),
    path('viewbook/<bookid>',views.viewbook),
    path('newbookandreview',views.newbookandreview),
    path('addreview/<bookid>',views.addreview),
    path('gohome',views.gohome),
    path('viewuser/<userid>',views.viewuser),
    path('boop/<reviewid>',views.boop),
]
