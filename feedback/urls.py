from django.urls import path
from .views import feedback_view, thank_you_view, feedback_graph

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('thank-you/', thank_you_view, name='thank_you'),
    path('feedback-graph', feedback_graph, name='feedback_graph'),

]
