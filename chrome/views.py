from django.shortcuts import render

# Create your views here.
def boost(request):
    d={'name':'BUBALUS BUBALIS','age':22}
    return render(request,'jinja.html',context=d)
