from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform_views(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        message=request.POST.get('message','')
        address=request.POST.get('address','')
        email=request.POST.get('email','')
        user_message=UserMessage()
        user_message.name=name
        user_message.email=email
        user_message.addresss=address
        user_message.message=message
        user_message.save()
    return render(request,'留言板.html')