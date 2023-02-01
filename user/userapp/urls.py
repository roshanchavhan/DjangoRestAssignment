from userapp import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name="register"),
    path('login/', views.LogInAPIView.as_view(), name="login"),
    path('logout/', views.LogOutAPIView.as_view(), name="logout"),
    path('delete/<int:pk>', views.DeleteAPIView.as_view(), name="delete"),
    path('update/<int:pk>', views.UpdateAPIView.as_view(), name="update"),
    path('changepassword/<int:pk>',views.ChangePasswordView.as_view(), name="change_password"),
    path('hello/', views.HelloView.as_view(), name ='hello'),
]
