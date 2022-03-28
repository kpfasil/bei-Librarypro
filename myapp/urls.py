from django.urls import path
from .views import *

urlpatterns = [
    path('home/',indexview),
    path('book/',booklistview),
    path('issuebook/',IssueBooKDetailView),
    path('add/<int:id>',IssueBookView,name='add'),
    path('user/',userlistview),
    path('adduser/',adduserview),
    path('',SigninView),
    path('logout/',logoutview),
]