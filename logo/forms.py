from django import forms
from .models import LogoForm
from django.core.mail import send_mail

class contactlogo(forms.ModelForm):
    #1
    pName = forms.CharField(required=True, max_length=50, label='عنوان پروژه:' , widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'pName', 'id':'pName', 'class':'form-control'}))
    
    cName = forms.CharField(required=True, max_length=50, label='نام مشتری:' , widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'cName', 'id':'cName', 'class':'form-control'}))
    
    bName = forms.CharField(required=True, max_length=50, label='نام برند:' , widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'bName', 'id':'bName', 'class':'form-control'}))
    
    service = forms.CharField(required=True, max_length=50, label='خدمت/سرویس/محصول:' , widget= forms.TextInput(attrs={'type':'text', 
                                            'name':'service', 'id':'service', 'class':'form-control'}))
    
    wPhone = forms.CharField(required=True, label='شماره تماس کسب و کار:', 
                                widget=forms.Textarea(attrs={'id':'wPhone', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'wPhone', 'value':"", 'class':'form-control' }),)
    
    pPhone = forms.CharField(required=True, label='تماس:', 
                                widget=forms.Textarea(attrs={'id':'pPhone', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'pPhone', 'value':"", 'class':'form-control' }),)
    
    email = forms.EmailField(required=True, label='ایمیل', widget= forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email', 'type':'email'}))

    sAddress = forms.CharField(required=True, label='آدرس شبکه های اجتماعی:', 
                                widget=forms.Textarea(attrs={'id':'sAddress', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'sAddress', 'value':"", 'class':'form-control' }),)

    #2
    bExplain = forms.CharField(required=True, label='شما چکار میکنید ؟ شغلتون رو توضیح بدید ؟ چه چیزی شغل شما رو منحصر به فرد یا متمایز میکنه ؟', 
                                widget=forms.Textarea(attrs={'id':'bExplain', 'rows': '5', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'bExplain', 'value':"", 'class':'form-control' }),)

    gExplain = forms.CharField(required=True, label='سعی دارید به چه کسانی دسترسی پیدا کنید؟ هدفتون چه کسانی هستند ؟', 
                                widget=forms.Textarea(attrs={'id':'gExplain', 'rows': '5', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'gExplain', 'value':"", 'class':'form-control' }),)

    #3
    nameInLogo = forms.CharField(required=True, label='چه نامی باید در لوگو درج شود ؟', 
                                widget=forms.Textarea(attrs={'id':'nameInLogo', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'nameInLogo', 'value':"", 'class':'form-control' }),)

    tags = forms.CharField(required=True, label='تگ لاین/برچسب', 
                                widget=forms.Textarea(attrs={'id':'tags', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'tags', 'value':"", 'class':'form-control' }),)

    isdExplain = forms.CharField(required=True, label='در صورت نیاز / وجود چه تصاویری باید در لوگو گنجانده شود ؟', 
                                widget=forms.Textarea(attrs={'id':'isdExplain', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'isdExplain', 'value':"", 'class':'form-control' }),)

    #extra Field

    isd = forms.CharField(required=True, label='تصویری/اشکال/طراحی', 
                                widget=forms.Textarea(attrs={'id':'isd', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'isd', 'value':"", 'class':'form-control' }),)

    usage = forms.CharField(required=True, label='مارک/برند تجاری، کارت ویزیت و غیره', 
                                widget=forms.Textarea(attrs={'id':'usage', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'usage', 'value':"", 'class':'form-control' }),)
    
    recommendation = forms.CharField(required=True, label='طراحی چند اتوده', 
                                widget=forms.Textarea(attrs={'id':'recommendation', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'recommendation', 'value':"", 'class':'form-control' }),)
    
    #4
    logoType = forms.CharField(required=True, label='لوگو تصویری لوگو نوشتاری(فارسی یا انگلیسی) یا تلفیقی باشد؟', 
                                widget=forms.Textarea(attrs={'id':'logoType', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'logoType', 'value':"", 'class':'form-control' }),)

    colorType = forms.CharField(required=True, label=' به صورت پیشفرض سیاه سفید است مگر اینکه برند شما رنگ خاصی داشته باشد', 
                                widget=forms.Textarea(attrs={'id':'colorType', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'colorType', 'value':"", 'class':'form-control' }),)

    example = forms.CharField(required=True, label=' آیا نمونه خارجی یا داخلی که میخواهید لوگوی خود از آن نمونه برداری شود دارید؟', 
                                widget=forms.Textarea(attrs={'id':'example', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'example', 'value':"", 'class':'form-control' }),)

    logomotion = forms.CharField(required=True, label='نیاز به لوگو موشن دارید؟', 
                                widget=forms.Textarea(attrs={'id':'logomotion', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'logomotion', 'value':"", 'class':'form-control' }),)
    
    budget = forms.CharField(required=True, label='بودجه خود را برای پروژه طراحی لوگو خود مشخص کنید', 
                                widget=forms.Textarea(attrs={'id':'budget', 'rows': '2', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'budget', 'value':"", 'class':'form-control' }),)


    class Meta:
        model=LogoForm
        fields=['pName', 'cName', 'bName', 'service', 
                'wPhone', 'pPhone', 'email', 'sAddress',
                'bExplain', 'gExplain', 'nameInLogo', 'tags',
                'isdExplain', 'isd', 'usage', 'recommendation',
                'logoType', 'colorType', 'example', 'logomotion', 'budget']

    def sendMail(self):
        if self.cleaned_data['email'] != '':
                 send_mail('ارسال موفقیت آمیز', 'your message is sended to us', 'contactToAnoushiravan@mailfa.com', [self.cleaned_data['email'], ])