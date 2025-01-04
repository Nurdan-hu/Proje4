from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.shortcuts import redirect
from okul.models import Kadro



# Create your views here.
def anasayfa(request):
  template = loader.get_template('anasf.html')
  return HttpResponse(template.render())

def isk(request):
  template = loader.get_template('isk.html')
  return HttpResponse(template.render())

def kulup(request):
  template = loader.get_template('kulup.html')
  return HttpResponse(template.render())

def kadro(request):
  aktarilacakListe  = Kadro.objects.all()
  sayfa = loader.get_template('kadro.html')
  giden ={
      'aktarilanListe' : aktarilacakListe,
  }
  return HttpResponse(sayfa.render(giden, request))



class OgretmenForm(forms.ModelForm):

  class Meta:
    model = Kadro
    fields = ['AdiSoyadi', 'Sinifi','Bransi' , 'Aciklama']


def ogretmenEkleme(request): # requestler/sorgulama kullanıcı bazlı düşünülür.
  if request.method == 'POST':
    form = OgretmenForm(request.POST)
    if form.is_valid():
      # Form verileri işleme
      form.save()  # Veritabanına kaydetme
      return redirect('liste')  #url name
  else:  # POST değil ise GET tir
    form = OgretmenForm()
  return render(request, 'ogretmenEkle.html', {'form': form})

def ogretmenSil (request, id):
    xxx = Kadro.objects.get(id=id)
    xxx.delete()
    return redirect('liste')

def ogretmenDuzenle(request, id):
  secilen_kayit = Kadro.objects.get(id=id)

  if request.method == 'POST': # Kullanıcı göndermiştir
      kayit_formu = OgretmenForm(request.POST, instance=secilen_kayit)
      if kayit_formu.is_valid():
          # Form verileri işleme
          kayit_formu.save()  # Veritab. kaydetme
          return redirect('liste') #url name
  else: # POST değil ise GET tir (Kullanıcı istemiştir)
      kayit_formu = OgretmenForm(instance=secilen_kayit)
  return render(request, 'ogretmenduzenle.html', {'form': kayit_formu})

def search (request):
 pass

def munazara (request):
  template = loader.get_template('munazara.html')
  return HttpResponse(template.render())

def voleybol (request):
  template = loader.get_template('voleybol.html')
  return HttpResponse(template.render())