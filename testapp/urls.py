from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', views.EmpListAPIView.as_view()),
    path('create/', views.EmpCreteAPIView.as_view()),
    path('retrieve/<int:id>/', views.EmpRetriveAPIView.as_view()),
    path('update/<int:id>/', views.EmpUpdateAPIView.as_view()),
    path('destroy/<int:id>/', views.EmpDestroyAPIView.as_view()),
    path('listcreate/', views.EmployeeListCreateAPIView.as_view()),
    path('retrieveupdatedestroy/<int:id>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
]
