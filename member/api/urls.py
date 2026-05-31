from django.urls import path
from member.api.views import memberlist, membercreate, memberdelete, memberupdate

urlpatterns = [
    path('', memberlist, name='member-list'),
    path('create/', membercreate, name='member-create'),
    path('update/<int:id>/', memberupdate, name='member-update'),
    path('delete/<int:id>/', memberdelete, name='member-delete'),
]