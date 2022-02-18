from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graph', views.graph, name='graph'),
    path('view_plot1', views.view_plot1, name='view_plot1'),
    path('view_plot2', views.view_plot2, name='view_plot2'),
    path('get_graph_data',views.get_graph_data,name="get_graph_data"),
]