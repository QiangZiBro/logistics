from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Details
from .forms import DeliveryForm, StatusForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'logsapp/home.html')


@login_required
def customer(request):
    return render(request, 'logsapp/customer.html')


@login_required
def deliveryform(request):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        if delivery_form.is_valid():
            deliveryform = delivery_form.save(commit=False)
            deliveryform.save()
            messages.success(request, f'Your order is registered. Pickup will be done within a day.')
            return redirect('customer')
    else:
        delivery_form = DeliveryForm()
    return render(request, 'logsapp/deliveryform.html', {'form': delivery_form})


def orders(request):
    order = Details.objects.filter(your_name=request.user)
    print(order)
    arg = {'ord': order}
    return render(request, 'logsapp/orders.html', arg)


def delivery(request):
    delivery = Details.objects.all()
    arg = {'ord': delivery}
    if request.method == "POST":
        a = request.POST['dropid']
        b = request.POST['dropstatus']
        obj = Details.objects.get(id=a)
        if b == True:
            obj.delivered = True
        else:
            obj.delivered = False
        obj.save()
    else:
        context_dict = {}
    # return render(request, 'demo/dashboard.html', context_dict)
    return render(request, 'logsapp/delivery.html', arg)
