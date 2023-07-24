from django.shortcuts import render

# Create your views here.

def HTML_Response(request):
    return render(request,'HTML_Response.html')