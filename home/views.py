from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages




# Create your views here.
def Index(request):
    clients =  Client.objects.all()
    
    context = {
        'clients': clients,}
    return render(request,('home.html'),context)



def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        project= request.POST.get('projectfield', None)
        value=request.POST.get('valuefield', None)
        mail=request.POST.get('mailfield', None)
        status=request.POST.get('statusfield', None)
        print(search_id)
        print(project)
        print(value)
        print(mail)
        print(status)
        cle = Client(client=search_id ,project=project,value=value,status=status,mail=mail)
        cle.save()
        clients =  Client.objects.all()
    
        context = {
            'clients': clients,}
        
        
        return render(request, 'home.html',context)
    else:
        print("hellockjdncjkjckjnklnkln")
        return render(request, 'home.html')

def delete(request,flight_id):
    c = Client.objects.get(pk=flight_id)
    c.delete()
    clients =  Client.objects.all()
    
    context = {
        'clients': clients,}
    return render(request,('home.html'),context)

def invoice(request,invoice_id):
    d = Client.objects.get(pk=invoice_id)
    context = {
        'client':d
    }
    return render(request,('invoice.html'),context)

def mail(request,mail_id):
    m = Client.objects.get(pk=mail_id)
    context = {
        'client':m
    }
    # send_mail(
    # 'Subject here',
    # 'Here is the message.',
    # 'ananthus991@gmailmail.com',
    # [m.mail],
    # fail_silently=False,html_message=render_to_string('invmail.html', context))
    m.status="Invoice Rised"
    m.save()
    clients =  Client.objects.all()
    
    context = {
        'clients': clients,}
    
    

    messages.error(request, 'Mail Has Been successfully Send ')
    return render(request,'home.html',context)
    
    return render(request,('invmail.html'),context)
