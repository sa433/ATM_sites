from django.db import models

class State(models.Model):
    sname = models.CharField(max_length=50)

    def __str__(self):
        return self.sname

class City(models.Model):
    cname = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname

class ATMSite(models.Model):
    bname = models.CharField(max_length=255)
    bid = models.CharField(max_length=10)
    baddress = models.TextField()
    persondetail = models.JSONField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)  # Add this line


    def __str__(self):
        return self.bname
