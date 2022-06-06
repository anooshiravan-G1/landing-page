from django import forms
#from django.forms import fields, models, widgets
from .models import Index
#from django.core.validators import validate_email
from django.core.mail import send_mail
from django.core.validators import RegexValidator


class contactMe(forms.ModelForm):

    name = forms.CharField(required=True, max_length=50, label='نام و نام خانوادگی(ضروری)' , widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'name', 'id':'name', 'class':'form-control'}))
    workName = forms.CharField(required=True, max_length=80, label='نام کسب و کار(ضروری)', widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'workName', 'id':'workName', 'class':'form-control'}))
    phone_number = forms.CharField(required=True, max_length=17, label='شماره تماس(ضروری)', widget= forms.NumberInput(attrs={'type':'text', 
                                            'name':'phoneNumber', 'id':'phoneNumber', 'class':'form-control'} ))
    email = forms.EmailField(required=False, label='ایمیل', widget= forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email', 'type':'email'}))
    socialName = forms.CharField(required=False, label='رسانه های کسب و کار', widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'socialMedia', 'id':'socialMedia', 'class':'form-control'} ))
    subject = forms.CharField(required=False, label='موضوع', widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'subject', 'id':'subject', 'class':'form-control'} ) )
    message = forms.CharField(label='پیام', widget=forms.Textarea(attrs={'id':'message', 'rows': '3', 'required data-error':'پیام خود را وارد کنید',
                                                                     'name':'message', 'value':"", 'class':'form-control' }),)

    class Meta:
        model=Index
        fields=['name', 'workName', 'phone_number', 'socialName', 'subject', 'email', 'message' ]

    def sendMail(self):
        if self.cleaned_data['email'] != '':
                 send_mail('ارسال موفقیت آمیز', 'your message is sended to us', 'contactToAnoushiravan@mailfa.com', [self.cleaned_data['email'], ])