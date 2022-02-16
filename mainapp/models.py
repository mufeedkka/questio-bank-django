from urllib import request
from django.db import models

# Create your models here.
class university(models.Model):
    university_name = models.CharField(max_length=100)
    def __str__(self):
        return self.university_name

class department(models.Model):
    university = models.ForeignKey(university, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def university_name(self):
        return self.university.university_name
    def __str__(self):
        return self.name

class subject(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    def department_name(self):
        return self.department.name
    def __str__(self):
        return self.subject

class questionanswer(models.Model):
    ques= models.TextField()
    answer=models.TextField()
    username=models.CharField(max_length=100)
    university_select = models.ForeignKey(university, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    year=models.IntegerField()
    show=models.BooleanField(default=False)
    timesAsked=models.CharField(max_length=2,blank=True,null=True)
    comment=models.CharField(max_length=500,null=True)
    important=models.BooleanField(default=False)
    def __str__(self):
        return self.ques[:30]
