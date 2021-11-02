from django.db import models

class Farmer(models.Model):
    fname = models.CharField("First_name", max_length=240)
    lname = models.CharField("Last_name", max_length=240)
    email = models.EmailField()
    address = models.CharField("address", max_length=240)
    username = models.CharField("username", max_length=240)
    password = models.CharField("password", max_length=240)

    def __str__(self):
        return self.username