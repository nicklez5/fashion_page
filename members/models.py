from django.db import models
class Men_Shirt(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='files/covers')
#
class Men_Jacket(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='files/covers')

class Men_Pants(models.Model):
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='files/covers')

class Men_Joggers(models.Model):
    waist_size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='files/covers')
class Men(models.Model):
    mens_shirt = models.ForeignKey(Men_Shirt, on_delete=models.CASCADE)
    mens_jacket = models.ForeignKey(Men_Jacket, on_delete=models.CASCADE)
    mens_pants = models.ForeignKey(Men_Pants,on_delete=models.CASCADE)
    mens_joggers = models.ForeignKey(Men_Joggers, on_delete=models.CASCADE)

class Glasses(models.Model):
    image = models.ImageField(upload_to="files/covers")
    price = models.FloatField

class Earring(models.Model):
    image = models.ImageField(upload_to="files/covers")
    price = models.FloatField

class Necklace(models.Model):
    image = models.ImageField(upload_to="files/covers")
    price = models.FloatField


class Accessories(models.Model):
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    earring = models.ForeignKey(Earring, on_delete=models.CASCADE)
    necklace = models.ForeignKey(Necklace, on_delete=models.CASCADE)


class Women_Shirt(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="files/covers")

class Women_Jacket(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="files/covers")

class Women_Pants(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="files/covers")

class Women_Joggers(models.Model):
    size = models.CharField(max_length=50)
    price = models.FloatField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="files/covers")

class Women(models.Model):
    women_shirt = models.ForeignKey(Women_Shirt, on_delete=models.CASCADE)
    women_jacket = models.ForeignKey(Women_Jacket, on_delete=models.CASCADE)
    women_pants = models.ForeignKey(Women_Pants,on_delete=models.CASCADE)
    women_joggers = models.ForeignKey(Women_Joggers,on_delete=models.CASCADE)
    
# Create your models here.
