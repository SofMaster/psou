from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):     #요청에 반응을 보이는 함수는 request를 인자로 줘야 한다.
    #return HttpResponse('요청 처리 결과')
    
    msg = '장고 만세'
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>" %msg
    return HttpResponse(ss)

def showFunc(request):
    msg = '파이썬 어쩌구 저쩌구'
    return render(request, 'show.html', {'mymsg':msg}) #forward 방식