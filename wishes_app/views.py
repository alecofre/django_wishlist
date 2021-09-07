from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import Item
from login_app.models import User


# Create your views here.
def dashboard(request):
     # all_items = Item.objects.all()
     user = User.objects.get(id = request.session['user']['id'] )
     my_items = user.mywhyshes.all()
     no_my_items = Item.objects.all().exclude(id__in = my_items)

     context = {
          'my_items' : my_items,
          'no_my_items' : no_my_items
     }
     return render(request,'wishes_app/dashboard.html',context)
     # return HttpResponse('Esta es la pagina del dashboard')

def create_wish_form(request):
     # pass
     return render(request,'wishes_app/create_wish.html')
     # return redirect('/dashboard')

def create_wish(request):
     if request.method == 'GET':
          return redirect('/')
     else:
          if request.method == 'POST':
               errors = Item.objects.validator_fields(request.POST)
               if len(errors) > 0 :
                    for key,value in errors.items():
                         messages.error(request,value)
                    return redirect("/wish_items/create")

               else:
                    article = request.POST['article']
                    user = User.objects.get(id = request.session['user']['id'])
                    new_item = Item.objects.create(article = article, creator = user)
                    new_item.save()
                    new_item.wisher.add(user)
     
                    return redirect('/dashboard')

def show_item(request, item_id):
     item = Item.objects.get(id = item_id)
     wishers = item.wisher.all()
     context = {
          'item' : item,
          'wishers' : wishers
     }
     return render(request,'wishes_app/show_item.html', context)

def add2MyList(request, item_id):
     item = Item.objects.get(id = item_id)
     user = User.objects.get(id = request.session['user']['id'])
     item.wisher.add(user)
     item.save()
     return redirect('/dashboard')


def remove2MyList(request, item_id):
     item = Item.objects.get(id = item_id)
     user = User.objects.get(id = request.session['user']['id'])
     item.wisher.remove(user)
     item.save()
     return redirect('/dashboard')

def delete(request, item_id):
     item = Item.objects.get(id = item_id)
     item.delete()
     return redirect('/dashboard')
