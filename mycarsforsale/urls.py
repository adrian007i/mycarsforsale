"""mycarsforsale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^login/',views.user_login,name='user_login'),
    url(r'^dets/',views.dets,name='dets'),
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^register/',views.RegistrationForm,name='RegistrationForm'),
    url(r'^logout/',views.logout_form,name='logout_form'),
    url(r'^upload/',views.upload,name='upload'),
    url(r'^delete_car/',views.delete_car,name='delete_car'),
    url(r'^edit_car/',views.edit_car,name='edit_car'),
    url(r'^edit_car_2/',views.edit_car_2,name='edit_car_2'),
    url(r'^filterSearch/',views.filterSearch,name='filterSearch'),
    url(r'^drafts/',views.drafts,name='drafts'),
    url(r'^alldrafts/',views.alldrafts,name='alldrafts'),
    url(r'^delete_post/',views.delete_post,name='delete_post'),
    url(r'^blog/',views.blog,name='blog'),
    url(r'^addComment/',views.addComment,name='addComment'),
    url(r'^publish_post/',views.publish_post,name='publish_post'),
    url(r'^delete_comment/',views.delete_comment,name='delete_comment'),
    url(r'^delete_entire_post/',views.delete_entire_post,name='delete_entire_post'),
    url(r'^edit_post/',views.edit_post,name='edit_post'),
    url(r'^edit_post_2/',views.edit_post_2,name='edit_post_2'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
