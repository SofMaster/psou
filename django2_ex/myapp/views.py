from django.shortcuts import render

# Create your views here.
def Mainfunc(request):
    return render(request, "main.html")

def SelectGender(request):
    if request.method == 'POST':
        gender = request.POST['gender']
        return render(request, "show.html",{"gender" : gender})
    else:
        print('요청 에러')
        