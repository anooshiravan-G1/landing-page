from django import forms
from .models import ProjectForm
from django.core.mail import send_mail

class contactProject(forms.ModelForm):

    #1
    challenge = forms.CharField(required=True, label='به طور مختصر چالش شرکت خود را شرح دهید:', 
                                widget=forms.Textarea(attrs={'id':'challenge', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'challenge', 'value':"", 'class':'form-control' }),)

    dates = forms.CharField(required=True, label='تاریخ ها(تا چه تاریخی میخواهید پروژه به انجام شود) و همچنین پیشرفت مورد انتظار را درج کنید.', 
                                widget=forms.Textarea(attrs={'id':'dates', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'dates', 'value':"", 'class':'form-control' }),)

    moreExplain = forms.CharField(required=True, label='موارد بیشتر درمورد پروژه:', 
                                widget=forms.Textarea(attrs={'id':'moreExplain', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'moreExplain', 'value':"", 'class':'form-control' }),)

    results = forms.CharField(required=True, label='هدف و نتایجه ای که از پروژه میخواهید:', 
                                widget=forms.Textarea(attrs={'id':'results', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'results', 'value':"", 'class':'form-control' }),)

    #2
    prjRequirements = forms.CharField(required=True, label='الزامات پروژه رو مشخص کنید:', 
                                widget=forms.Textarea(attrs={'id':'prjRequirements', 'rows': '4', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'prjRequirements', 'value':"", 'class':'form-control' }),)

    wyLike = forms.CharField(required=True, label='کار هایی که دوست دارید انجام شود ولی صد  در صد لازم نیست:', 
                                widget=forms.Textarea(attrs={'id':'wyLike', 'rows': '4', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'wyLike', 'value':"", 'class':'form-control' }),)

    limits = forms.CharField(required=True, label=' محدودیت هایی که برای پروژه در نظر گرفتید:', 
                                widget=forms.Textarea(attrs={'id':'limits', 'rows': '4', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'limits', 'value':"", 'class':'form-control' }),)

    #3
    goals = forms.CharField(required=True, label='اهداف اولیه درمورد پروژه،یعنی هدفی که قراره به آن دست پیدا کنید،حل کردن مشکلات بقیه،همراه کردن مشتریان با خود و ...', 
                                widget=forms.Textarea(attrs={'id':'goals', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'goals', 'value':"", 'class':'form-control' }),)

    measurement = forms.CharField(required=True, label='نحوه سنجش موفقیت را با استفاده از معیارهای خاص مشخص کنید:', 
                                widget=forms.Textarea(attrs={'id':'measurement', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'measurement', 'value':"", 'class':'form-control' }),)

    audience = forms.CharField(required=True, label='مشخص کنید که مخاطب چه کسی است، دید شما برای ادامه پروژه چیست، و نکات اصلی مشکل  مشتری را مشخص کنید.', 
                                widget=forms.Textarea(attrs={'id':'audience', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'audience', 'value':"", 'class':'form-control' }),)

    problems = forms.CharField(required=True, label='مخاطب ثانویه و مشکلات آن ها در ضمینه کاری خود را مشخص کنید', 
                                widget=forms.Textarea(attrs={'id':'problems', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'problems', 'value':"", 'class':'form-control' }),)
    
    #4
    introduction = forms.CharField(required=True, label='نام شرکت ، نام و نام خانوادگی خود را وارد کنید.', 
                                widget=forms.Textarea(attrs={'id':'introduction', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'introduction', 'value':"", 'class':'form-control' }),)
    connection = forms.CharField(required=True, label='شماره تماس و یا ایمیل خود را برای برقراری ارتباط وارد کنید.', 
                                widget=forms.Textarea(attrs={'id':'connection', 'rows': '3', 'required data-error':'لطفا این فیلد را کامل کنید',
                                'name':'connection', 'value':"", 'class':'form-control' }),)


    class Meta:
        model=ProjectForm
        fields=['challenge', 'dates', 'moreExplain', 'results', 
                'prjRequirements', 'wyLike', 'limits',
                'goals', 'measurement', 'audience', 'problems',
                'introduction', 'connection']

    def sendMail(self):
        if self.cleaned_data['email'] != '':
                 send_mail('ارسال موفقیت آمیز', 'your message is sended to us', 'contactToAnoushiravan@mailfa.com', [self.cleaned_data['email'], ])