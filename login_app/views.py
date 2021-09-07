from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import date,datetime
import bcrypt

from .models import User

# Create your views here.
def login_page(request):
     return render(request, 'login_app/login.html')

def register(request):
     if request.method == 'GET':
          return redirect('/')
     else:
          if request.method == 'POST':
               errors = User.objects.validator_fields(request.POST)
               # messages.error(request,len(errors))

               if len(errors) > 0 :
                    for key,value in errors.items():
                         messages.error(request,value)
                    request.session['registro_name'] = request.POST['name']
                    request.session['registro_username'] = request.POST['username']

                    request.session['level_message'] = 'alert-danger'

               else:
                    request.session['registro_name'] = ""
                    request.session['registro_username'] = ""

                    name = request.POST['name']
                    username = request.POST['username']
                    dateHired = datetime.strptime(request.POST['date_hired'],'%Y-%m-%d').date()

                    password = request.POST['password']
                    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

                    new_user = User.objects.create(name=name, username=username,password=pw_hash, dateHired=dateHired)
                    new_user.save()
                    messages.success(request,"Nuevo usuario registrado!!")
                    request.session['level_message'] = 'alert-success'
               return redirect('login_page')
          return redirect('/')

def login(request):
     if request.method == 'GET':
          return redirect('/')

     if request.method == 'POST':

          request.session['registro_name'] = ""
          request.session['registro_username'] = ""

          username = request.POST['username_login']
          user_eval = User.objects.filter(username = username)
          if len(user_eval) > 0 :

               user_to_login = user_eval[0]
               password = request.POST['password_login']

               if bcrypt.checkpw( password.encode() , user_to_login.password.encode()):
                    user = {
                         'id' : user_to_login.id,
                         'name' : user_to_login.name,
                         'username' : user_to_login.username,
                    }

                    request.session['user'] = user
                    request.session['login_email'] = ''
                    return redirect('/dashboard')

               else:
                    messages.error(request,'Password mal ingresada o usuario no está registrado!!')
                    return redirect('login_page')

          else:
               messages.error(request,'Datos mal ingresados o usuario no está registrado!!')
               return redirect('login_page')

     return render(request,'login.html')

def logout(request):
     request.session.flush()
     return redirect('login_page')
