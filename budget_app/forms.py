from .models import Expense, Budget
from django.contrib.auth.models import User
from django import forms
# from . import validators
#from django.core import validators

class UserReg(forms.ModelForm):
    number = forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','password','email','number']

    def save(self, commit=True):
        user = super(UserReg, self).save(commit=False)
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user

class UserLogin(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput,
                               # validators = [validators.NumberValidator,
                               #               validators.UppercaseValidator,
                               #               validators.LowercaseValidator,
                               #               validators.SymbolValidator,
                                             )

class Add_t(forms.Form):
    date = forms.DateField()
    amount = forms.FloatField()
    desc = forms.CharField(max_length=20)
    category = forms.CharField(max_length=20)

class Add_b(forms.Form):
    budget_amt = forms.FloatField()
    date = forms.DateField()
    category = forms.CharField(max_length=15)


def clean_password(self):
    password = self.cleaned_data['password']
    if len(password) < 4:
        raise forms.ValidationError("Password too short")
    return password

