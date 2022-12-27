
# Add your urls here for stuff

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('see_all/',views.see_all),
    path('<int:roll>/',views.student),
    path('search/',views.search),
    path('ent_info/',views.ent_info),
    path('completed/',views.completed),
    path('update/',views.update),
    path('update/<int:roll_no>/',views.update_roll)
]
