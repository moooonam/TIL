import random
from django.shortcuts import render

# Create your views here.
def index(request):
    # request : 사용자의 요청 정보가 담겨있다.
    # 사용자에게 보여줄 화면 html 파일이름
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ["치킨","피자","삼겹살",]
    info = {"name":"짱구"}
    context = {
        "foods" : foods,
        "info" : info,        
        }
    return render(request, 'articles/greeting.html', context)
def dinner(request):
    foods = ["치킨","피자","삼겹살","수박","텐동",]
    pick = random.choice(foods)
    words = "가 나 다 라 마 바 사 아 자 차 카 타 파 하"
    my_num = [1,2,3,4,5,6,7,8,9]
    context ={
        'pick':pick,
        'foods':foods,
        'words':words,
        'my_num':my_num,
    }
    return render(request, 'articles/dinner.html',context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))

    message = request.GET.get('message')
    content = {
        'message':message,
    }
    return render(request, "articles/catch.html", content)

def hello(request, name):
    context = {
        'name':name,
    }
    return render(request, 'articles/hello.html',context)