from pickle import TRUE
from django.db import models

# Create your models here.
class ProjectForm(models.Model):
    #1
    challenge = models.TextField('چالش شرکت', null=False, blank=False)
    dates = models.TextField('تاریخ انجام پروژه', null=False, blank=False)
    moreExplain = models.TextField('توضیحات بیشتر درباره پروژه', null=False, blank=False)
    results = models.TextField('اهداف و نتایج پروژه', null=False, blank=False)
    #2
    prjRequirements = models.TextField('الزامات پروژه', null=False, blank=False)
    wyLike = models.TextField('ترجیحات پروژه', null=False, blank=False)
    limits = models.TextField('محدودیت های پروژه', null=False, blank=False)
    #3
    goals = models.TextField('اهداف اولیه پروژه', null=False, blank=False)
    measurement = models.TextField('روش های سنجش پروژه', null=False, blank=False)
    audience = models.TextField('مخاطب های پروژه', null=False, blank=False)
    problems = models.TextField('مشکلات پیاده سازی پروژه', null=False, blank=False)
    #4
    introduction = models.TextField('معرفی خود', null=False, blank=False)
    connection = models.TextField('راه های ارتباطی', null=False, blank=False)


    def __str__(self):
        return self.introduction
