from django.shortcuts import render, redirect
from django.db import models
from django.utils.decorators import method_decorator
from django.core.handlers.wsgi import WSGIRequest

from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.contrib.admin.widgets import AdminDateWidget

from typing import Callable

from .models import *


class LogoutViewICPS(LogoutView):
    next_page="../../"
    template_name="login.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.next_page = "../../" if request.META.get('HTTP_REFERER') == None else request.META.get('HTTP_REFERER')
        return super().dispatch(request, *args, **kwargs)

class LoginViewICPS(LoginView):
    next_page="../../"
    prev_page="/"
    template_name="login.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        self.prev_page = self.next_page if request.META.get('HTTP_REFERER') == None else request.META.get('HTTP_REFERER')
        self.next_page = self.next_page if self.prev_page == f"http://{request.get_host()}{request.get_full_path()}" else self.prev_page
        print(self.prev_page)
        print(f"http://{request.get_host()}{request.get_full_path()}")
        return super().dispatch(request, *args, **kwargs)



def main(request):
    return render(request, "index.html", {})

