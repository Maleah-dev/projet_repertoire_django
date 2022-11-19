from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact
from .forms import contactForm


# Create your views here.
def acceuil(request):
    contacts=contact.objects.all()
    context={'contacts':contacts}
    return render(request,'contact/liste_contact.html',context)
    #return render(request,'contact/liste_contact.html')
    #return HttpResponse("bonjour")
    
def liste_contact(request,pk):
    contact1=contact.objects.get(id=pk)
    context={'contact1':contact1}
    return render(request,'contact/details.html',context)

def ajouter_contact(request):
    form=contactForm()
    if request.method=='POST':
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'contact/ajouter_contact.html',context)


def modifier_contact(request,pk):
    contact2=contact.objects.get(id=pk)
    form=contactForm(instance=contact2)
    if request.method=='POST':
        form=contactForm(request.POST,instance=contact2)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'contact/ajouter_contact.html',context)