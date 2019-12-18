from django.db import models
from django.urls import reverse


# Create your models here.

class intro(models.Model):
    name  = models.TextField(max_length = 120)
    email = models.TextField(blank = False ,null = False)
    contatc_num = models.IntegerField(max_length = 11)
    additional_info = models.TextField(blank = True,null = True)
    address = models.TextField(blank=False,null=False)

    def get_absolute_url(self):
        return reverse("dynamicc", kwargs={"my_id": self.id})
    
      #f"/dynamics/{self.id}/"
