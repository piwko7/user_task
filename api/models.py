from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=500)
    # address
    street = models.CharField(max_length=128)
    suite = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    # geo
    geo_lat = models.FloatField()
    geo_lng = models.FloatField()

    phone = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    # company
    company_name = models.CharField(max_length=128)
    company_catchPhrase = models.CharField(max_length=128)
    company_bs = models.CharField(max_length=128)

    def __str__(self):
        return f'Name: {self.name} - Username: {self.username}'

    class Meta:
        verbose_name_plural = "Users"


class Todos(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_todos')
    title = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'userId: {self.userId} - Title: {self.title}'

    class Meta:
        verbose_name_plural = "Todos"

