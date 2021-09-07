from django.db import models
from login_app.models import User


# Create your models here.
class ItemManager(models.Manager):
     def  validator_fields(self, postData):

          errors = {}
 
          if ( len(postData['article'].strip()) < 3 ):
               errors['article_len'] = 'Nombre del artículo debe tener al menos 3 caracteres'
 
          return errors




class Item(models.Model):
    article = models.CharField(max_length=128, blank=False, null=False)
    creator = models.ForeignKey(User, related_name='myitems', on_delete=models.CASCADE)
    wisher  = models.ManyToManyField(User, related_name='mywhyshes', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ItemManager()


    def __repr__(self) -> str:
         return self.article

    def __str__(self) -> str:
         return self.article

