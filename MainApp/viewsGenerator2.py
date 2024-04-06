from django.db import models

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.decorators import classonlymethod

from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.admin.widgets import AdminDateWidget

from .models import *
from .helper import notLoggedUsers, getAllFields


def lowerFirstLetter(string):
    return string[0].lower() + string[1:]

def getTemplateDir(model):
    try:
        return {
            Teacher: "teacher/",
            Attestation: "attestation/",
            Student: "student/",
            TaskResult: "taskResult/",
            Task: "task/"
        }[model]
    except:
        return ""

def getTemplatePath(model, operationName):
    return f"{lowerFirstLetter(getTemplateDir(model))}/{operationName.lower()}.html"

class CRUDBinder:
    model: models.Model

    bindedCreateView: CreateView
    bindedUpdateView: UpdateView
    bindedDeleteView: DeleteView
    bindedListView: ListView

    def __init__(self, model: models.Model,
            bindedCreateView: CreateView,
            bindedUpdateView: UpdateView,
            bindedDeleteView: DeleteView,
            bindedListView: ListView ):
        self.model = model
        self.bindedCreateView = bindedCreateView
        self.bindedUpdateView = bindedUpdateView
        self.bindedDeleteView = bindedDeleteView
        self.bindedListView = bindedListView

class FormCustomizingICPSMixin():
    def customizingForm(form, model, user):
        def teacherCustomize(form):
            form.fields['user'].queryset = User.objects.filter(id=user.id)
        def attestationCustomize(form):
            form.fields['teacher'].queryset = Teacher.objects.filter(user_id=user.id)
            form.fields['date'].widget = AdminDateWidget(attrs={'type': 'date'})
        try:
            {
                Teacher: teacherCustomize,
                Attestation: attestationCustomize
            }[model](form)
        except:
            return



class BindedViewMixin:
    @classonlymethod
    def bindingCRUD(self, binder: CRUDBinder):
        self.binder = binder
        self.model = self.binder.model
        self.fields = list(getAllFields(self.binder.model))
        self.success_url = "successful.html"


def createView(binderP, ViewType):
    @method_decorator(notLoggedUsers, name='dispatch')
    class BindedView(BindedViewMixin, ViewType):
        binder = binderP
        model = binder.model
        fields = list(getAllFields(binder.model))
        success_url = "successful.html"

        @classonlymethod
        def as_view(self):
            return BindedView.as_view(self)

        def get_form(self, form_class=None):
            form = super(BindedView, self).get_form(form_class)
            form.title = self.binder.model.__name__
            self.binder.customizingForm(form, self.model, self.request.user)
            return form

    return BindedView


@method_decorator(notLoggedUsers, name='dispatch')
class BindedUpdate(BindedViewMixin, UpdateView):
    @classonlymethod
    def as_view(self, binder):
        BindedViewMixin.bindingCRUD(self, binder)
        return super().as_view()

    def get_form(self, form_class=None):
        form = super(BindedUpdate, self).get_form(form_class)
        form.title = (str)(self.binder.model.objects.get(id=self.kwargs["pk"]))
        self.binder.customizingForm(form, self.model, self.request.user)
        return form

@method_decorator(notLoggedUsers, name='dispatch')
class BindedRead(BindedViewMixin, ListView):
    @classonlymethod
    def as_view(self, binder):
        BindedViewMixin.bindingCRUD(self, binder)
        return super().as_view()

@method_decorator(notLoggedUsers, name='dispatch')
class BindedDelete(BindedViewMixin, DeleteView):
    @classonlymethod
    def as_view(self, binder):
        BindedViewMixin.bindingCRUD(self, binder)
        return super().as_view()


