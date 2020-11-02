from django import forms
from .models import Menu,Oder,Reviews,Contant,OrderIn,OrderI
from django.shortcuts import get_object_or_404
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout,Submit,Row,Column

class PlaceOrder(forms.ModelForm):

    class Meta:
        model = OrderIn
        fields = ['meal','table_number']
        #'name', 'phone_number'
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
class PlaceOrderI(forms.ModelForm):

    class Meta:
        model = OrderI
        fields = ['table_number', 'meal_1', 'meal_2', 'meal_3', 'meal_4', 'meal_5', 'meal_6']


class OrderIn1(forms.ModelForm):

    class Meta:
        model = Oder
        fields = [ 'phone_number']

class OrderIn2(forms.ModelForm):

    class Meta:
        model = Oder
        fields = ['meal', 'name', 'phone_number']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [ 'name', 'your_experience']

class ContantUs(forms.ModelForm):

    class Meta:
        model = Contant
        fields = ['your_name', 'email', 'subject', 'message']
