from Match.views import *
from .views import *
from django.urls import path,include

urlpatterns = [
    path("Make/Jobs/Mine/all",MakeAllJobs),
    path("Make/Jobs/Add/Phase",addPhase),
    path("Add/Default/SQ",addSq),
]

