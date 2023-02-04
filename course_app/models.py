from django.db import models

# Create your models here.
class Instructor(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name= models.CharField(max_length=20)
    rating = models.IntegerField()
    instructor= models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses') 
