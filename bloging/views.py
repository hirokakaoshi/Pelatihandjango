# Create your views here.
import datetime
from django.http import HttpResponse #bsia juga disingkat jadi import HttpResponse as res
#mengimportr shortcut untuk helper
from django.shortcuts import render_to_response
#menambah CSRF
from django.template import RequestContext
#mngimport artikel untuk ditampilkan dari models
from bloging.models import Artikel
#import form di bloging buat tampiolan form meureunan
from bloging.form import FormArtikel


def sekarang(request):
    sekarang = datetime.datetime.now()
    return HttpResponse(sekarang) # kalau singaktan dipakai maka HttpResponse bisa diganti jadi res

def home(request):
    artikel = Artikel.objects.all()
    return render_to_response('home.html', {
               'Gudang_Artikel' : artikel
           })
    #return HttpResponse(artikel)

def baca(request,id_artikel):
    artikel = Artikel.objects.get(id=id_artikel)
    return render_to_response('baca.html',{
         'artikel' : artikel
    })

def sunting(request):
    #ini untuk posting dan sunting
    if request.method == "POST" :
       form = FormArtikel(request.POST)
       if form.is_valid() : 
          form.save()
    return render_to_response('sunting.html',{
         'form' : FormArtikel()
    },RequestContext(request))
