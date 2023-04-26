from django.db import models
import uuid

class BasicBranch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

class BasicAddress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    township = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street} {self.township} {self.city} {self.state} {self.country}-{self.zip_code}"
    

class BasicPhoneDetails(models.Model):
    phone_type = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    country_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country_code} {self.phone_no}"