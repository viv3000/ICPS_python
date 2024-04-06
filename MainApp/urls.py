from django.urls import path
from django.apps import apps
from django.urls import include
from django.contrib.auth import views as auth_views

from . import views
from .includeCRUD import includeCRUD

urlpatterns = [
    path("", view=views.main),
    path("accounts/logout/",  views.LogoutViewICPS.as_view() ),
    path("accounts/login/", views.LoginViewICPS.as_view()),
    path("change-password/", auth_views.PasswordChangeView.as_view()),
        ]

for model in apps.all_models['MainApp'].values():
    print(model)
    urlpatterns.append(path(f'{model.__name__}',  view=includeCRUD(model) ) )
