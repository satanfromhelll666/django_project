"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  v
Including another URLconf
    1. Import th
def print_test(request,*args, **kwargs):
    
    obj = self.object.get(id=1)

    test = {
        'name' : obj.name,
        'email' : obj.email

    }
    return render(request,"test_1.htm",test)e include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from view.views import print_intro,print_address
from self.views import print_test,print_test_form,dinamic_look
from self.views import print_test2
from self.views import dinamic_look,dinamic_look_delete,intro_list_view



urlpatterns = [
    path('address/', print_address, name='home'),
    path('', print_intro, name='home'),
    path('form/', print_test_form, name='home'),
    path('admin/', admin.site.urls),
    path('test/',print_test),
    path('test1/',print_test2),
    path('dynamics/<int:my_id>/',dinamic_look,name='dynamicc'),
    path('dynamic/<int:my_id>/delete/',dinamic_look_delete,name='dynamic-delete'),
    path('listview/',intro_list_view),
]
