from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class ClasseForm(ModelForm):
    class Meta:
        model = models.Classe
        fields = ('nom_classe', 'formation', 'date_debut', 'nombre_etudiants','details')
        labels = {
            'nom_classe' : _('Nom de la classe'),
            'formation' : _('Formation de la classe') ,
            'date_debut' : _('Date de début de l\'année scolaire'),
            'nombre_etudiants' : _('La note moyenne de la classe'),
            'details' : _('Détails')
        }

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom_etudiant', 'pays_naissance', 'date_naissance', 'moyenne','details', 'classe')
        labels = {
            'nom_etudiant': _('Nom d\'étudiant'),
            'pays_naissance': _('Pays de naissance'),
            'date_naissance': _('Date de naissance'),
            'moyenne': _('La note moyenne d\'étudiant '),
            'Détails': _('Détails'),
            'classe' : _("Classe:")
        }

class Etudiant_ajoutForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom_etudiant', 'pays_naissance', 'date_naissance', 'moyenne', 'details')
        labels = {
            'nom_etudiant': _('Nom d\'étudiant'),
            'pays_naissance': _('Pays de naissance'),
            'date_naissance': _('Date de naissance'),
            'moyenne': _('La note moyenne d\'étudiant '),
            'Détails': _('Détails'),
        }