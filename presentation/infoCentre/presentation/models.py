from django.db import models
import datetime
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
    def nom(self):
        return self.link

    code=models.CharField(max_length=100, unique=True,blank=False)
    nom=models.CharField(max_length=200,default="None")  
    link=models.TextField(blank=False, max_length=5000)
    description= models.TextField( max_length=5000,blank=True)
    height= models.PositiveIntegerField(default=1000)



class Parent_frame(models.Model):

    def __str__(self):
        return self.code

    def code(self):
        return self.code

    def nom(self):
        return self.link

    def description(self):
        return self.description
        
    code=models.CharField(max_length=100, unique=True,blank=False)
    nom=models.TextField(blank=False, max_length=5000)
    description= models.TextField( max_length=5000,blank=True)
    kibanas_frame = models.ManyToManyField(Kibana_frame)




class Parent_kibana_frame(models.Model):
    Kibana_frame = models.ForeignKey(Kibana_frame, on_delete=models.CASCADE)
    Parent_frame = models.ForeignKey(Parent_frame, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)



    