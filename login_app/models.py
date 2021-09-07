from django.db import models
from datetime import date,datetime
import re

# Create your models here.
class UserManager(models.Manager):
     def  validator_fields(self, postData):
          JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')
          PASSWORD_REGEX = re.compile(r'^(?=\w*[a-zA-Z.])\S{8,16}$')
          # PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')
 
          errors = {}
 
          if len(User.objects.filter(username = postData['username'])) > 0 :
              errors['username_exists'] = 'username no disponible'
          else:
               if ( len(postData['name'].strip()) < 3 ):
                   errors['name_len'] = 'Nombre debe tener al menos 3 caracteres'

               if ( len(postData['username'].strip()) < 3 ):
                   errors['username_len'] = 'Username debe tener al menos 3 caracteres'
  
               if ( len(postData['password'].strip()) < 8 ):
                   errors['password_len'] = 'Password debe tener al menos 8 caracteres sin espacios'
  
               if not JUST_LETTERS.match(postData['username']):
                   errors['solo_letras'] = 'El username sólo debe contener letras, sin espacios'

               now = date.today()
               dh = datetime.strptime(postData['date_hired'],'%Y-%m-%d').date()
               diff_date = now - dh
               diff_days = diff_date.days

               if diff_days < 0:
                    errors['bad_date'] = 'La fecha de registro no puede ser una fecha futura'
               
               if not PASSWORD_REGEX.match(postData['password']):
                   errors['bad_pw'] = "Formato de contraseña no válido. "
  
               if postData['password'] != postData['password_confirm']:
                   errors['nosame_pw'] = 'Contraseñas no coinciden'
 
          return errors



class User(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, default="name")
    username = models.CharField(max_length=16, null=False, blank=False, unique=True, default='username')
    password = models.CharField(max_length=256)
    dateHired = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self) -> str:
         return self.username

    def __str__(self) -> str:
         return self.username
