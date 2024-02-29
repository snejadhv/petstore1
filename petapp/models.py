from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    breed = models.CharField(max_length= 100)
    profile_image = models.ImageField(upload_to='profile_images/',null=True , blank= True)

    def __str__(self):
        return f"{self.name} {self.breed},{self.price}"