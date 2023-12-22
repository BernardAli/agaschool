from django.contrib import admin

from accounts.models import (CashCenter, IncomeExpenditure)

# Register your models here.


admin.site.register(CashCenter)
admin.site.register(IncomeExpenditure)