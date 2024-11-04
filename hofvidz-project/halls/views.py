from django.shortcuts import render
#auth imp for class based 
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request,'halls/home.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name  ='registration/signup.html'


# def createcreate_hall(request):
#     if request.method == "POST":
#         #get form data
#         #validate form data 
#         #create hall 
#         # save hall:
#     else:    
#         #create a form for a hall 
#         # create template

