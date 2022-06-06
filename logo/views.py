from django.views.generic import FormView #,TemplateView 
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from .forms import contactlogo
from django.core import serializers


class logoView(FormView):
    template_name='logoForm.html'
    success_url='/confirmLogo/'
    form_class=contactlogo





def logoConfirm(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = contactlogo(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            #messages.add_message(request, messages.success, 'پیام با موفقیت ارسال شد')
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            #messages.error(request,'username or password not correct')
            #return JsonResponse({"error": form.errors}, status=400)
            return redirect('logo')
    # some error occured
    #messages.error(request,'username or password not correct')
    #return JsonResponse({"error": ""}, status=400)
    return redirect('logo')