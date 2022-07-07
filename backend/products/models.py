from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title.title()

    @property
    def sale_price(self):
        return f"{float(self.price)*0.8:.2f}"
