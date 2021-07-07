# Create your views here.
from django import template
from django.contrib.admin.options import ModelAdmin
from django.db.models.aggregates import Sum
from django.db.models.base import Model
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import UserReg, UserLogin, Add_t, Add_b
from .models import Budget, Expense, People
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
import numpy as np
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    template = loader.get_template('sign-up.html')
    if request.method=='POST':
        form=UserReg(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            data=form.cleaned_data
            usr=data['username']
            pas=data['password']
            eml=data['email']
            nmb=data['number']
            a=People()
            a.username=usr
            a.password=pas
            a.email=eml
            a.number=nmb
            a.save()
            user.set_password(pas)

            user.save()
            user=authenticate(username=usr,password=pas)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')

            return HttpResponse('<h1>VALID</h1>')
        return HttpResponse(template.render({'form':form},request))
    else:
        return HttpResponse(template.render({},request))
	#return render(request, 'sign-up.html')

def log(request):
    template = loader.get_template('login.html')
    if request.method=='POST':
        form=UserLogin(request.POST)
        if form.is_valid():

            data=form.cleaned_data
            username=data['username']
            password=data['password']
            user=authenticate(username=username,password=password)

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return render(request,'transaction_success.html')

            return HttpResponse('<h1>Invalid Credentials</h1>')
        return HttpResponse('<h1>invalid Data</h1>')
    else:
        return HttpResponse(template.render({}, request))

def logout(request):
    auth.logout(request)
    return redirect("http://127.0.0.1:8000/")

def main(request):
    return render(request, 'main.html')

def transaction_success(request):
    expense_items = Expense.objects.all()
    return render(request, 'transaction_success.html', {'data':expense_items})

def add_item(request):
    template = loader.get_template('add.html')
    if request.method=='POST':
        form=Add_t(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            data=form.cleaned_data
            date=data['date']
            amount=data['amount']
            desc=data['desc']
            category=data['category']
            a=Expense()
            a.date=date
            a.amount=amount
            a.desc=desc
            a.category=category
            a.save()
            return HttpResponseRedirect('transaction_success/')
            # expense_items = Expense.objects.order_by('date')
            # context = {'expense_items' : expense_items}
            # return render(request, 'transaction_success.html', context=context)
        return HttpResponse(template.render({'form':form}, request))
    else:
        return HttpResponse(template.render({},request))

def add_budget(request):
    template = loader.get_template('add_budget.html')
    if request.method=='POST':
        form=Add_b(request.POST)
        if form.is_valid():
            # user=form.save(commit=False)
            data=form.cleaned_data
            budget_amt=data['budget_amt']
            date=data['date']
            category=data['category']
            a=Budget()
            a.budget_amt = budget_amt
            a.date=date
            a.category=category
            a.save()
            return HttpResponseRedirect('budget_success/')
            # expense_items = Expense.objects.order_by('date')
            # context = {'expense_items' : expense_items}
            # return render(request, 'transaction_success.html', context=context)
        return HttpResponse(template.render({'form':form}, request))
    else:
        return HttpResponse(template.render({},request))

def budget_success(request):
    budget_items = Budget.objects.all()
    return render(request, 'budget_success.html', {'data':budget_items})


def myview(request):
    data = export_csv(ModelAdmin, request, Expense.objects.all())
    return HttpResponse(data, content_type = 'text/csv')

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Expense.csv;'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"date"),
        smart_str(u"Amount"),
        smart_str(u"description"),
        smart_str(u"category"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.date),
            smart_str(obj.amount),
            smart_str(obj.desc),
            smart_str(obj.category),
        ])
    return response
export_csv.short_description = u"Export CSV"


def report(request):
    return render(request, 'reports.html')
