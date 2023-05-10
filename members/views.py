from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Men_Shirt,Men_Jacket
from .forms import UploadForm
# Create your views here.

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def men_shirt(request, men_shirt_id):
    men_shirt = Men_Shirt.objects.get(pk=men_shirt_id)
    if men_shirt is not None:
        return render(request, 'men_shirt.html',{'MenShirt':men_shirt})
    else:
        raise Http404("Shirt does not exist")

def men_jacket(request,men_jacket_id):
    men_jacket = Men_Jacket.objects.get(pk=men_jacket_id)
    if men_jacket is not None:
        return render(request,'men_jacket.html',{'MenJacket': men_jacket})
    else:
        raise Http404("Jacket does not exist")

def men_pants(request,men_packet_id):
    men_pants = Men_Pants.objects.get(pk=men_pants_id)
    if men_pants is not None:
        return render(request,'men_pants.html',{'MenPants': men_jacket})
    else:
        raise Http404("Pants does not exist")
def upload(request):
    if request.POST:
        form = UploadForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        redirect(members)
    return render(request, 'upload.html',{'form': UploadForm})