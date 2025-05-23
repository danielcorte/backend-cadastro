from django.urls import path

from .views import views_prof, views_disc, views_ambi, views_curs, views_turm, views_regs
from django.views.decorators.csrf import csrf_exempt

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
    path('disc/search/', views_disc.DisciplinasSearchView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('ambientes', views_ambi.listar_ambientes),
    path('ambi', views_ambi.AmbientesView.as_view()),
    path('ambi/id/<int:pk>', views_ambi.AmbientesDetailView.as_view()),
    path('ambi/search/', views_ambi.AmbientesSearchView.as_view()),

    path('cursos', views_curs.listar_cursos),
    path('curs', views_curs.CursosView.as_view()),
    path('curs/id/<int:pk>', views_curs.CursosDetailView.as_view()),
    path('curs/search/', views_curs.CursosSearchView.as_view()),

    path('turmas', views_turm.listar_turmas),
    path('turm', views_turm.TurmasView.as_view()),
    path('turm/id/<int:pk>', views_turm.TurmasDetailView.as_view()),
    path('turm/search/', views_turm.TurmasSearchView.as_view()),

    path('cadastro', csrf_exempt(views_regs.CreateUserView.as_view())),
]