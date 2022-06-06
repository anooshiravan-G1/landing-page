from django.views.generic import FormView #,TemplateView 
from .forms import contactMe
from django.http import HttpResponseRedirect
from django.contrib import messages



class indexView(FormView):
    template_name='Index.html'
    success_url='/confirm/'
    form_class=contactMe

    def form_valid(self, form):
        if self.request.method == "POST":
            if form.is_valid():
                if form.cleaned_data['phone_number'].isnumeric()==True:
                    form.save()
                    #form.sendMail()
                    messages.success(self.request, 'پیام با موفقیت ارسال شد')
                    return HttpResponseRedirect('')
                else:
                    messages.warning(self.request, 'خطا در ارسال')
                    return HttpResponseRedirect('')
            

