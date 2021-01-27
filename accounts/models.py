from django.db import models

 
# Create your models here.
class StudentForm(models.Model):  
    firstname = models.CharField("Enter name", max_length=50)  
    file      = models.FileField() # for creating file input  
  
    class Meta:  
        db_table = "pictures"