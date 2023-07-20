from app_cad_usuarios import views # tenho que sempre importar do app as view para redirecionar na rota
from django.urls import path
#descrevendo o path
# path('',views.home,name='home'),
# depois de fazer from app_cad... importando views, você criar o path que é o caminho
#path(' aqui vai o nome do dominio exemplo cadastro.com', views.nome_da_views para ser criada, name='nome da views criada e seu caminho')
urlpatterns = [
    # vai criar rota, view responsavel, nome de referencia
    path('', views.home, name='home'),

    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
