
from django import forms  
from accounts.models import StudentForm  #models.py
    
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentForm  
        fields = "__all__"