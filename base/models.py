from django.db import models

# Create your models here.
class Contact(models.Model):
    fristname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(default ='')
    massage = models.CharField(default = '' , max_length=50)

    def __str__(self):
        return self.fristname
