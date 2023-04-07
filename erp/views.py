from django.shortcuts import render, redirect

# HttpResponse: 응답에 대한 메타정보를 가지고 있는 객체
from django.http import HttpResponse
from .models import Product

def erp_in(request):
    if request.method == 'POST':  # 요청 방식이 POST 일때
        name = request.name  # 현재 로그인 한 사용자를 불러오기
        quantity = request.POST.get("my-content", "")
        my_erp = Product.objects.create(name=name, quantity=quantity)
        my_erp.save()
    return redirect('/home')
    #     my_erp = Product()  # 글쓰기 모델 가져오기
    #     my_erp.name = name  # 모델에 사용자 저장
    #     my_erp.quantity = request.POST.get('quantity', '')
    #     my_erp.save()
    # return redirect('/erp')
    
def gogohome(request):
    return redirect('/home')