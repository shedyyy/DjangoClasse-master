from django.db import models

class Classe(models.Model):
    nom_classe = models.CharField(max_length=100)
    formation = models.CharField(max_length = 100)
    date_debut = models.DateField(blank = True, null = True)
    nombre_etudiants = models.IntegerField(blank = False)
    details = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nom_classe}"
        return chaine

    def dico(self):
        return {"nom_classe": self.nom_classe, "formation": self.formation,"date_debut":self.date_debut,"nombre_etudiants": self.nombre_etudiants,"details": self.details}

class Etudiant(models.Model):
    nom_etudiant = models.CharField(max_length=100)
    pays_naissance = models.CharField(max_length=100)
    date_naissance = models.DateField(blank=True, null=True)
    moyenne = models.IntegerField(blank=False)
    details = models.TextField(null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,default= None, null=True)

    def __str__(self):
        chaine = f"{self.nom_etudiant}"
        return chaine

    def dico(self):
        return {"nom_etudiant": self.nom_etudiant, "pays_naissance": self.pays_naissance,"date_naissance":self.date_naissance,"moyenne": self.moyenne,"details": self.details,"classe":self.classe}