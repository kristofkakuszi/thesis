from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#
from django.shortcuts import render  
from django.http import HttpResponse  
from accounts.functions import handle_uploaded_file  #functions.py
from accounts.forms import StudentForm #forms.py


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

  
def index(request):  
    if request.method == 'POST':  
        pictures = StudentForm(request.POST, request.FILES)  
        if pictures.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            model_instance = pictures.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        pictures = StudentForm()  
        return render(request,"index.html",{'form':pictures}) 

