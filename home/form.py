from django import forms
from .models import Menu,Oder,Review,Contant
from django.shortcuts import get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout,Submit,Row,Column

class PlaceOrder(forms.ModelForm):
  
    class Meta:
        model = Oder 
        fields = ['meal', 'name', 'phone_number']
    '''def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('meal', css_class='form-group col-md-6-mb-0'),
                Column('name', css_class='form-group col-md-6-mb-0'),
                Column('phone_number', css_class='form-group col-md-6-mb-0'),
                css_class='form-row'

            ),
            Submit('submit', 'Place Order')
        )'''

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['myphoto', 'name', 'your_experience', 'facebook', 'twitter', 'instagram']

class ContantUs(forms.ModelForm):
    
    class Meta:
        model = Contant
        fields = ['your_name', 'email', 'subject', 'message']
