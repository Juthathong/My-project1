from django.shortcuts import render,redirect
from django.http import HttpResponse
from myhotel.models import Clientsinfo
from myhotel.models import RoomAvailable

# Create your views here.
def index(request):
    return render(request,("index.html"))
def accommodation(request):
    return render (request,("accommodation.html"))
def form(request):
    return render(request,("form.html"))
# def accommodation(request):
#     if request.method=="POST":
#         checkin=request.POST["checkin"]
#         checkout=request.POST["checkout"]
#         print(checkin)
#         roomAvailable = RoomAvailable.objects.create(
#             checkindate=checkin,
#             checkoutdate=checkout
#         )
#         roomAvailable.save()
#         return render("accommodation.html") 
#     else:
#         redirect ("/")


