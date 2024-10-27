from django.shortcuts import render
from hookah.models import HookahTobacco
from django.views import View
from hookah.forms import TobaccoForm

# Create your views here.

#region hookah CRUD
def hookahList(request):
    hookahs = HookahTobacco.objects.all().order_by('-registeredDay')
    return render(request, 'hookah/CRUD/hList.html', {'hookahs': hookahs})

class TobaccoCreate(View):
    templateList = 'hookah/CRUD/tobaccoCreate.html'

    def get (self,request):
        form = TobaccoForm()
        return render(request, self.templateList, {'form':form})
    
    def post (self,request):
        form = TobaccoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hookahList')
        return render(request, self.templateList, {'form':form})
