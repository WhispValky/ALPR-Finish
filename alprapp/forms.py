from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms 
from django.forms import ModelForm 
from .models import Post

class DateInput(forms.DateInput):
    input_type = 'date'

class AddCarForm(ModelForm):
    class Meta:
        model = Post
        fields = ["car_plate", "car_name", "car_owner", "car_color", "published_date"]

        widgets = {
            'published_date': DateInput()
}

class UpdateCarForm(ModelForm):
    class Meta:
        model = Post
        fields = ["car_name", "car_owner", "car_color", "published_date"]

        widgets = {
            'published_date': DateInput()
}