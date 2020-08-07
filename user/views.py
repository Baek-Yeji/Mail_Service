from django.shortcuts import render, redirect
import json
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from user.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
class SignUpView(View):
    def post(self,request,*args,**kwargs):
        user_id = request.post['user_id']
        password = request.POST['password']
        user_name = request.POST['user_name']
        user_tel = request.POST['user_tel']

        user = User(
            user_id = user_id,
            password = password,
            user_name = user_name,
            user_tel = user_tel,
        )
        user.save()
        return redirect("user:login")

    def get(self, request,*args,**kwargs):
        return render(request,'user/signup.html')

class LoginView(View):
    def post(self, request):
        print(request.POST);
        user_id = request.POST['user_id']
        password = request.POST['password']
        try:
            # 필드명 = 조건값을 인자로 가지며, 해당 데이터가 유일하게 존재해야함.
            user = User.objects.filter(user_id=user_id,password = password)
            print(user[0].id)
            check = True
        except User.DoesNotExist:
            check = False
        if check:
            print("인증성공")
            save_session(request, user[0].id, user_id,password)
            return redirect("user:mail")
        else:
            print("인증실패")
            return render(request,'user/login.html')
        return render(request,'user/login.html')

    def get(self, request):
        return render(request,'user/login.html')
    
def save_session(request,id,user_id,password):
    request.session['id'] = id
    request.session['user_id'] = user_id
    request.session['password'] = password
        
        
class mailView(View):
    def post(self,request):
        return HttpResponse("mail-post")
    def get(self, request):
        return render(request,'user/mail.html')

class LogoutView(View):
    def post(self, request):
        return HttpResponse("logout-post")
    def get(self, request):
        logout(request)
        return redirect("user:login")
    

def id_overlap_check(request):
    user_id = request.GET.get('user_id')
    try:
        user = User.objects.get(user_id = user_id)
    except User.DoesNotExist:
        user = None
    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"
    context = {'user_id':user_id,'overlap':overlap}
    return JsonResponse(context)


class ModifyView(View):
    def post(self, request):
        id = request.session['id']
        user_mo_id = request.POST['user_id']
        user_mo_ps = request.POST['password']
        user_mo_name = request.POST['user_name']
        user_mo_tel = request.POST['user_tel']
        user = User(
            id = id,
            user_id = user_mo_id,
            password = user_mo_ps,
            user_name = user_mo_name,
            user_tel = user_mo_tel,
        )
        user.save()
        return redirect('user:login')
    def get(self,request):
        return render(request,'user/modify.html')




    