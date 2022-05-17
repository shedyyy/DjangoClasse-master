from django.urls import path
from . import views
urlpatterns = [
    path('',views.main),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('traitementupdate/<int:id>',views.traitementupdate),
    path('ajoutt/', views.ajoutt),
    path('ajouttt/<int:id>/', views.ajouttt),
    path('traitementt/', views.traitementt),
    path('traitementtt/<int:id>/', views.traitementtt),
    path('updatee/<int:id>/',views.updatee),
    path('deletee/<int:id>/',views.deletee),
    path('traitementupdatee/<int:id>',views.traitementupdatee),
]