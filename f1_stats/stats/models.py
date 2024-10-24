from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    length_km = models.FloatField()

    def __str__(self):
        return self.name

class Constructor(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Standing(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    season = models.IntegerField()
    points = models.FloatField()
    position = models.IntegerField()

    def __str__(self):
        return f"{self.driver.name} - {self.season}"
