from django.shortcuts import render
from django.http import HttpResponse

 
def post_list(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'form.html',{})
