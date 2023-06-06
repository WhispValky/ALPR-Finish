from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .filters import Car_Plate_Filter
from .forms import AddCarForm, UpdateCarForm


@login_required
def HomePage(request):
    return render(request, "alprapp/HomePage.html",)

@login_required
def login(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'car_system/login.html', {'posts': posts})

@login_required
def thirdpage(request):
    alprapp = Post.objects.all()
    car_plate_filter = Car_Plate_Filter(request.GET, queryset=alprapp)
    context = { 
        "car_plate_filter": car_plate_filter,
        "title": "Search",
        "alpr": alprapp,
    }
    return render(request, "alprapp/third.html", context=context)

@login_required
def per_car_view(request, pk):
    alprapp = get_object_or_404(Post, pk=pk)
    context = {
        'alprapp': alprapp,
        "title": "Car Information",
    }

    return render(request, "alprapp/per_car.html", context=context)

@login_required
def delete_car(request, pk):
    alprapp = get_object_or_404(Post, pk=pk)
    alprapp.delete()
    messages.warning(request, "Car Deleted")
    return redirect("/HomePage/CarList/")

@login_required
def register(request):
    add_form = AddCarForm()
    if request.method == "POST":
        add_form = AddCarForm(data=request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, "Car Added")
            return redirect("/HomePage/CarList/")
  
    return render(request, "alprapp/register.html", {"form": add_form})

@login_required
def update_car(request, pk):
    alprapp = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        updateForm = UpdateCarForm(data=request.POST)
        if updateForm.is_valid():
            alprapp.car_name = updateForm.data['car_name']
            alprapp.car_owner = updateForm.data['car_owner']
            alprapp.car_color = updateForm.data['car_color']
            alprapp.published_date = updateForm.data['published_date']
            messages.info(request, "Car Updated")
            alprapp.save()

            return redirect("/HomePage/CarList/")

            
    else:
        updateForm = UpdateCarForm(instance=alprapp)

    context = {"form": updateForm}
    return render(request, "alprapp/update_car.html", context=context)

