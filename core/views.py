from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'profileList.html')
        return render(request, 'index.html')


@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, 'profileList.html', {'profiles' : profiles})


class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profileCreate.html')