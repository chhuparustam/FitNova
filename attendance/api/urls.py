from django.urls import path
from attendance.api.views import AttendanceAPIView

urlpatterns = [
    path('update/<int:id>/', AttendanceAPIView.as_view(), name='attendance_api'),
]