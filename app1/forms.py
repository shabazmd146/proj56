from django import forms
from app1.models import car
#create your forms here

class cars(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'