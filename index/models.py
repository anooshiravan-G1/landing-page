from pickle import TRUE
from django.db import models
from django.core.validators import RegexValidator

PHONEREGEX = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تماس وارد شده صحیح نمی باشد.", code='invalid_phoneNumber')
# Create your models here.
class Index(models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=50, null=False, blank=False)
    workName = models.CharField('نام کسب و کار', max_length=80, null=False, blank=False)
    

    phone_number = models.CharField('شماره تماس', validators=[PHONEREGEX], max_length=17, blank=False, null=False)
    
    email = models.EmailField('ایمیل', null=True, blank=TRUE)

    socialName = models.TextField('رسانه های کسب و کار', null=True, blank=True) 
    subject = models.CharField('موضوع', null=True, blank=True, max_length=120)
    message = models.TextField('متن پیام', null=True, blank=True)


    def __str__(self):
        return self.message
