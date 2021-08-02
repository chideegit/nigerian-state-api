from django.urls import path 

from .views import StateList, GovernorList

urlpatterns = [
    path('state-list/', StateList.as_view(), name='state-list'),
    path('governor-list/', GovernorList.as_view(), name='governor-list')
]

