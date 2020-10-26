from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import json

from webmaster.models import SettingsModel
from django.http import JsonResponse

class SettingsService():
    
    def __init__(self):
        pass

    
    def settingService(self, request):
        instance = self.get_instance()
        if instance:
            context = {}
            context['username'] = instance.username
            context['password'] = instance.password
            context['frequencyfollow'] = instance.frequencyfollow
            context['frequencyunfollow'] = instance.frequencyunfollow
            context['frequencypostcheck'] = instance.frequencypostcheck
            context['daysafterunfollow'] = instance.daysafterunfollow
            context['suspicion'] = instance.suspicion
            context['suspicioncode'] = instance.suspicioncode
            context['emailsuspicion'] = instance.emailsuspicion
            if instance.state is True:
                context['slider'] = 'Checked'
            else :
                context['slider'] = None
            
            return render(request, 'index.html', context)
        else:
            context = {}
            context['username'] = None
            context['password'] = None
            context['frequencyfollow'] = None 
            context['frequencyunfollow'] = None
            context['frequencypostcheck'] = None
            context['daysafterunfollow'] = None
            context['suspicioncode'] = None
            context['suspicion'] = None
            context['emailsuspicion'] = None
            return render(request, 'index.html', context)

    def createOrUpdate(self, request):
        instance = self.get_instance()
        # print('instance  : ', request.POST.get('slider'))
        if request.POST.get('slider') == 'on':
            botState = True
        else :
            botState = False

        if instance:
            instance.username = request.POST.get('username')
        else:
            instance = SettingsModel(username=request.POST.get('username'))

        instance.password = request.POST.get('password')
        instance.frequencyfollow = request.POST.get('frequencyfollow')
        instance.frequencyunfollow = request.POST.get('frequencyunfollow')
        instance.frequencypostcheck = request.POST.get('frequencypostcheck')
        instance.daysafterunfollow = request.POST.get('daysafterunfollow')
        instance.emailsuspicion = request.POST.get('emailsuspicion')
        instance.state = botState 
        instance.save()


        return HttpResponseRedirect(reverse('webmaster:Index'))

    def submitCode(self, request):
        code = json.loads(request.body)
        code = code['code']
        instance = self.get_instance()
        print('code  ',code)
        if instance and len(code) == 6:
            instance.suspicioncode = code
            instance.suspicion = False
            instance.save()
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'fail'})

    def get_instance(self):
        try:
            return SettingsModel.objects.get(id=1)
        except SettingsModel.DoesNotExist:
            print('except')
            print(SettingsModel.objects.all())
            return None


        