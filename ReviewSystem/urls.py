
from django.urls import path
from . import views
urlpatterns = [
    path('',views.candidate_list),
    path('candidatedetailed/<int:id>',views.candidate_detailed),
    path('list/',views.candidate_list),
    path('candidatecreate/', views.candidate_create)

]
