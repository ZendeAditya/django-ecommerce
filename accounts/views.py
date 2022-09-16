from django.shortcuts import render
from django.views import View
from .forms import UserSignUp
class SignUpView(View):
    def get(self,request):
        form = UserSignUp()
        context = {
            'form':form
        }  
        return render(request,'accounts/signup.html',context)