from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClasseForm, EtudiantForm, Etudiant_ajoutForm

from . import models

def ajout(request):
    if request.method == "POST":
        form = ClasseForm(request)
        if form.is_valid():
            classe = form.save()
            return HttpResponseRedirect("/IUTdeColmar/")
        else:
            return render(request,"iut/ajout.html",{"form": form})
    else:
        form = ClasseForm()
        return render(request,"iut/ajout.html",{"form" : form})

def ajoutt(request):
    if request.method == "POST":
        form = EtudiantForm(request)
        if form.is_valid():
            etudiant = form.save()
            return HttpResponseRedirect("/IUTdeColmar/")
        else:
            return render(request,"iut/ajoutt.html",{"form": form})
    else:
        form = EtudiantForm()
        return render(request,"iut/ajoutt.html",{"form": form})

def ajouttt(request , id):

        form = Etudiant_ajoutForm()
        return render(request,"iut/ajouttt.html",{"form": form,"id":id})

def traitement(request):
    cform = ClasseForm(request.POST)
    if cform.is_valid():
        classe = cform.save()
        return HttpResponseRedirect("/IUTdeColmar/")
    else:
        return render(request,"iut/ajout.html",{"form": cform})

def traitementt(request):
    jform = EtudiantForm(request.POST)
    if jform.is_valid():
        classe = jform.save()
        return HttpResponseRedirect("/IUTdeColmar/")
    else:
        return render(request,"iut/ajoutt.html",{"form": jform})

def traitementtt(request , id):
    aform = Etudiant_ajoutForm(request.POST)
    classe= models.Classe.objects.get(pk=id)
    if aform.is_valid():
        etudiant_ajout = aform.save(commit=False)
        etudiant_ajout.classe_id = id
        etudiant_ajout.classe = classe
        etudiant_ajout.save()
        return HttpResponseRedirect(f"/IUTdeColmar/affiche/{id}/")
    else:
        return render(request, "iut/ajouttt.html", {"form": aform, "id": id})

def main(request):
    classe = list(models.Classe.objects.all())
    return render(request, 'iut/home.html', {'liste': classe})


def affiche(request, id):
    classe = models.Classe.objects.get(pk=id)
    etudiant = list(models.Etudiant.objects.filter(classe_id=id))
    return render(request,"iut/affiche.html",{"classe": classe,"etudiant": etudiant})

def delete(request, id):
    classe = models.Classe.objects.get(pk=id)
    classe.delete()
    return HttpResponseRedirect("/IUTdeColmar/")

def deletee(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/IUTdeColmar/affiche/" + str(etudiant.classe_id) + "/")


def update(request, id):
    classe = models.Classe.objects.get(pk=id)
    cform = ClasseForm(classe.dico())
    return render(request, "iut/update.html", {"form": cform, "id": id})

def updatee(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    jform = EtudiantForm(etudiant.dico())
    return render(request, "iut/updatee.html ", {"form": jform, "id": id})

def traitementupdate(request, id):
    cform = ClasseForm(request.POST)
    if cform.is_valid():
        classe = cform.save(commit=False)
        classe.id = id
        classe.save()
        return HttpResponseRedirect("/IUTdeColmar")
    else:
        return render(request, "iut/update.html", {"form": cform, "id": id})

def traitementupdatee(request, id):
    jform = EtudiantForm(request.POST)
    if jform.is_valid():
        etudiant = jform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/IUTdeColmar")
    else:
        return render(request, "iut/updatee.html", {"form": jform, "id": id})

def traitementupdateee(request, id):
    jform = EtudiantForm(request.POST)
    if jform.is_valid():
        etudiant = jform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/IUTdeColmar")
    else:
        return render(request, "iut/updateee.html", {"form": jform, "id": id})