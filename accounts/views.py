
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel
from erp.models import Product
# from .form import CreateUserForm
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.


# def register(request):
#     if request.method =='POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid(): #유효하면 저장하라
#             form.save()
#             return redirect('dashboard-index') # erp??
#     else:
#         form = CreateUserForm()
#     context = {
#         'form':form,


#     }
#     return render(request, 'accounts/signup.html',context)
def gohome(request):
    return render(request,'accounts/signin.html')
    # user = request.user.is_authenticated
    # if user:
    #     return redirect("/home")
    # else:
    #     return redirect("/sign-in")

# def home(request):
#     return render(request, 'erp/home.html')
    

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:  # 로그인이 되어있다면
            return redirect('/')
        else:  # 로그인이 되어있지 않다면
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            return render(request, 'accounts/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'accounts/signup.html') # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in') # 회원가입이 완료되었으므로 로그인 페이지로 이동


# user/views.py
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            all_product = Product.objects.all()
            return render(request, 'erp/home.html',{"product":all_product})
        else:
            return render(request,'accounts/signin.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})  # 로그인 실패
    elif request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 로그인 되어 있는지 검사
        if user:  # 로그인이 되어 있다면
            return redirect('/')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'accounts/signin.html')
        
@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("/")
