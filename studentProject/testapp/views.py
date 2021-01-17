from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def home_page_view(request):
    students=Student.objects.all()
    return render(request,'testapp/index.html',{'students':students})
