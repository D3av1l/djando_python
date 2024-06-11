from django.shortcuts import render
def inicio(request):
    print("request",request)
    print ("has llamado a inicio")
    return render(request,"inicio.html")
