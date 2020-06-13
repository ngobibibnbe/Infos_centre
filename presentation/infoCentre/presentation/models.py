from django.db import models

# Create your models here.


class Kibana_frame(models.Model):

    def __str__(self):
        return self.code+" ------- "+self.link
    def code(self):
        return self.code
    def link(self):
        return self.link
    def description(self):
        return self.description
    code=models.CharField(max_length=100)
    link=models.TextField
    description= models.TextField






    