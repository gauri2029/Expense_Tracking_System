# Create your views here.
from django import template
from django.db.models.aggregates import Sum
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


# def transaction_success(request):
#     expense_items = Expense.objects.order_by('date')
#     try:
#         budget_total = Expense.objects.aggregate(budget = Sum('amount', filter = Q(amount_gt = 0)))
#         expense_total = Expense.objects.aggregate(expenses = Sum('amount', filter = Q(amount_lt = 0)))
#         fig, ax = plt.subplots()
#         ax.bar(['Expenses', 'Budget'], [abs(expense_total['expenses']), budget_total['budget']], color = ['red', 'green'])
#         ax.set_title('Total Expense VS Total Budget')
#         plt.savefig('expense_system/static/expense_system/expense.jpg')
#     except TypeError:
#         print('No data')
#     context = {'expense_items':expense_items, 'budget':budget_total['budget'], 'expenses':abs(expense_total['expenses'])}
#     return render(request, 'transaction_success.html', context = context)

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



# def transaction_success(request):
#     Expense.objects.create(date = date, amount = amount, desc = desc, category = category)
#     budget_total = Expense.objects.aggregate(budget = Sum('amount', filter = Q(amount_gt = 0)))
#     expense_total = Expense.objects.aggregate(expenses = Sum('amount', filter = Q(amount_lt = 0)))
#     fig, ax = plt.subplots()
#     ax.bar(['Expenses', 'Budget'], [abs(expense_total['expenses']), budget_total['budget']], color = ['red', 'green'])
#     ax.set_title('Total Expense VS Total Budget')
#     plt.savefig('expense_system/static/expense_system/expense.jpg')
#     return HttpResponseRedirect('transaction_success/')







    # date = request.POST.get('date')
    # amount = request.POST.get('amount')
    # desc = request.POST.get('desc')
    # category = request.POST.get('category')

# def add_transaction(request):
#     if request.method == 'POST':
#         print('post method')
#         # create a form instance and populate it with data from the request:
#         form = Add_Transaction(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             data = form.cleaned_data
#             a = Expense()
#             a.date=data['date']
#             a.amount=data['amount']
#             a.desc = data['desc']
#             a.category = data['category']
#             a.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('transaction_success/')
#     else:
#         form = Add_Transaction()
#     return render(request, 'add_transaction.html', {'form':form})

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = Add_Transaction()
    #     print('not post method')

    # data = Expense.objects.all()
    # return render(request, 'add_transaction.html', {'data': data})




    # if request.method == 'POST':
    #     form = Add_Transaction(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         a = Expense()
    #         a.date=data['date']
    #         a.amount=data['amount']
    #         a.desc = data['desc']
    #         a.category = data['category']
    #         a.save()
    #         return redirect('transaction_success/')
    #     else:
    #         return HttpResponse('<h1>Invalid Data</h1>')
    # a = Expense.objects.all()
    # context = {'data' : a}
    # return render(request, 'add_transaction.html', {'data' : a})
