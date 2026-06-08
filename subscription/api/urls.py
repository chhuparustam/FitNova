from django.urls import path

from subscription.api.views import SubscriptionView, SubscriptionUpdateAndDelete, GymMemeberView, MembershipPayment


urlpatterns = [
    path('', SubscriptionView.as_view(), name="subscription"),
    path('<int:pk>', SubscriptionUpdateAndDelete.as_view(),name="Subscription-update"),
    path('member',GymMemeberView.as_view()),
    path('payment/<int:id>',MembershipPayment.as_view())
]