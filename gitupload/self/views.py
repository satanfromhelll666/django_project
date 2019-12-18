from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import intro
from .form import intro_form
from django.http import Http404

# Create your views here.


def print_test_form(request,*args, **kwargs):
    
    form = intro_form(request.POST or None) 
    if form.is_valid():
        form.save()
        form = intro()
        form = intro_form()

    test1 = {
        'form' : form 

    }
    return render(request,"test_2.htm",test1)


def print_test(request,*args, **kwargs):
    
    #obj = intro.objects.get(id=1)

    test = {
        'object' : 123, #here you should use ','
        'my_list' : [20,25,'hello','nice']

    }
    return render(request,"test_1.htm",test)

def dinamic_look(request,my_id):
    #obj = intro.objects.get(id=my_id)
    obj = get_object_or_404(intro,id=my_id)

    contex={
        'object' : obj
    }

    return render(request,"temp/db.htm",contex)

def dinamic_look_delete(request,my_id):
    #obj = intro.objects.get(id=my_id)
    obj = get_object_or_404(intro,id=my_id)
    
    if request.method == 'GET':
        obj.delete()

    contex={
        'object' : obj
    }

    return render(request,"temp/delete.htm",contex)

def intro_list_view(request):
    queryset = intro.objects.all()
    contex={
        'object_list' : queryset
    }

    return render(request,"temp/objectlist.htm",contex)



def print_test2(request,*args, **kwargs):
    
    obj = intro.objects.get(id=1)
    obj2 = intro.objects.all();

    test = {
        'object' : obj

    }
    return render(request ,"temp/getdatafromDB.htm",test)

