from django.db import models

# Create your models here.

class Question(models.Model):

    def __str__(self):
        return self.question_text
    def question(self):
        return self.question_text
    def pub_date(self):
        return self.pub_date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):

    def __str__(self):
        return self.question_text
    def choice_text(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):

    def __str__(self):
        return self.first_name+" "+self.last_name
    def roles(self):
        return self.roles
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    roles= models.CharField(max_length=100)






    