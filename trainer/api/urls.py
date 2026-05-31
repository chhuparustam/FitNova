from django.urls import path

from trainer.api.views import TrainerUpdateDelete, TrainerView


urlpatterns = [
    path('', TrainerView.as_view(), name="trainer"),
    path('<int:pk>/', TrainerUpdateDelete.as_view(), name="Trainer-update-delete"),
]