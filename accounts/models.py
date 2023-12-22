from PIL import Image
from django.db import models
from django.urls import reverse

from authy.models import User


# Create your models here.


class CashCenter(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='payments.png', upload_to='payments')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cash_center_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super(CashCenter, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 500:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class IncomeExpenditure(models.Model):
    center = models.ForeignKey(CashCenter, on_delete=models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    receipt_number = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    amount_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    paid_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='paid_by')
    paid_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='paid_to')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("income_detail", kwargs={"pk": self.pk})