from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerModelForm

def customerView(request):
    if request.method == 'POST':
        customerForm = CustomerModelForm(request.POST)
        if customerForm.is_valid():
            customerForm.save()

    customerForm = CustomerModelForm()
    return render(request, 'customerForm.html', {'form': customerForm})