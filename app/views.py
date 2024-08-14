from django.shortcuts import render

from app.forms import ImageForm
from app.models import Image

# Create your views here.
def home(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    img=Image.objects.all()
    form=ImageForm()
    return render(request,'home.html',{'form':form,'img':img})