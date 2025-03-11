from django.urls import path

from .views import views_prof, views_disc

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('professores', views_prof.listar_professores),
    path('prof', views_prof.ProfessoresView.as_view()),
    path('prof/id/<int:pk>', views_prof.ProfessoresDetailView.as_view()),
    path('prof/search/', views_prof.ProfessoresSearchView.as_view()),

    path('disciplinas', views_disc.listar_disciplinas),
    path('disc', views_disc.DisciplinasView.as_view()),
    path('disc/id/<int:pk>', views_disc.DisciplinasDetailView.as_view()),
    path('disc/search/', views_prof.ProfessoresSearchView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]