from django.urls import path
from .views import SignUpView, LoginView, mailView, LogoutView, ModifyView
from . import views

app_name = "user"
urlpatterns = [
    path('signup',SignUpView.as_view(), name="signup"),
    path('login',LoginView.as_view(), name="login"),
    path('mail',mailView.as_view(), name ="mail"),
    path('logout',LogoutView.as_view(), name="logout"),
    path('id_overlap_check',views.id_overlap_check, name="id_overlap_check"),
    path('ModifyView',ModifyView.as_view(), name="ModifyView"),
]