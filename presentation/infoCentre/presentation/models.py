from django.db import models

# Create your models here.


class Kibana_frame(models.Model):

    def __str__(self):
        return self.code

    def code(self):
        return self.code

    def link(self):
        return self.link

    def description(self):
        return self.description
        
    code=models.CharField(max_length=100, unique=True,blank=False)
    link=models.TextField(blank=False, max_length=5000)
    description= models.TextField( max_length=5000,blank=True)
    height= models.PositiveIntegerField(default=1000)







    