from django.db import models

# Create your models here.
class LogoForm(models.Model):
    #1
    pName = models.CharField('عنوان پروژه:', max_length=50, null=False, blank=False)
    cName = models.CharField('نام مشتری:', max_length=50, null=False, blank=False)
    bName = models.CharField('نام برند:', max_length=50, null=False, blank=False)
    service = models.CharField('خدمت/سرویس/محصول:', max_length=50, null=False, blank=False)
    wPhone = models.TextField('شماره تماس کسب و کار:', null=False, blank=False)
    pPhone = models.TextField('تماس:', null=False, blank=False)
    email = models.EmailField('ایمیل', null=True, blank=False)
    sAddress = models.TextField('آدرس شبکه های اجتماعی:', null=False, blank=False)
    #2
    bExplain = models.TextField('شما چکار میکنید ؟ شغلتون رو توضیح بدید ؟ چه چیزی شغل شما رو منحصر به فرد یا متمایز میکنه ؟', null=False, blank=False)
    gExplain = models.TextField('سعی دارید به چه کسانی دسترسی پیدا کنید؟ هدفتون چه کسانی هستند ؟', null=False, blank=False)
    #3
    nameInLogo = models.TextField('چه نامی باید در لوگو درج شود ؟', null=False, blank=False)
    tags = models.TextField('تگ لاین/برچسب', null=False, blank=False)
    isdExplain = models.TextField('در صورت نیاز / وجود چه تصاویری باید در لوگو گنجانده شود ؟', null=False, blank=False)
    #extra field
    isd = models.TextField('تصویری/اشکال/طراحی', null=False, blank=False)
    usage = models.TextField('مارک/برند تجاری، کارت ویزیت و غیره', null=False, blank=False)
    recommendation = models.TextField('طراحی چند اتوده', null=False, blank=False)
    #4
    logoType = models.TextField('لوگو تصویری لوگو نوشتاری(فارسی یا انگلیسی) یا تلفیقی باشد؟', null=False, blank=False)
    colorType = models.TextField(' به صورت پیشفرض سیاه سفید است مگر اینکه برند شما رنگ خاصی داشته باشد', null=False, blank=False)
    example = models.TextField(' آیا نمونه خارجی یا داخلی که میخواهید لوگوی خود از آن نمونه برداری شود دارید؟', null=False, blank=False)
    logomotion = models.TextField('نیاز به لوگو موشن دارید؟', null=False, blank=False)
    budget = models.TextField('راه های ارتباطی', null=False, blank=False)


    def __str__(self):
        return self.cName


