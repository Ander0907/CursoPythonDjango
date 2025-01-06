from django.urls import path
from .views import ListPending, DetailWorkItem, CreateWorkItem, UpdateWorkItem, DeleteWorkItem

urlpatterns = [
    path('', ListPending.as_view(), name='pendings'),
    path('item/<int:pk>', DetailWorkItem.as_view(), name='details'),
    path('create-work-item/', CreateWorkItem.as_view(), name='create-work-item'),
    path('update-work-item/<int:pk>', UpdateWorkItem.as_view(), name='update-work-item'),
    path('delete-work-item/<int:pk>', DeleteWorkItem.as_view(), name='delete-work-item'),
]
