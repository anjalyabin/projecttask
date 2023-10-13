from django.db import models

# Create your models here.






class MyModel(models.Model):
    name = models.CharField(max_length=200,null=False)
    date = models.DateField()
    age =models.IntegerField(max_length=200,null=True)

    mobile =models.IntegerField(max_length=200,null=True)


    address = models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.name

