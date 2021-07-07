from budget_app.views import export_csv
from django.contrib import admin
from .models import Expense
# Register your models here.
class MyModel(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Expense, MyModel)