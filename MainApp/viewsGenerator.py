import os

from django.contrib.auth.models import models
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from .helper import notLoggedUsers, getAllFields

def createViewType(model: models.Model, BaseViewType, operationName, success="successful.html"):
    @method_decorator(notLoggedUsers, name="dispatch")
    class CreatedViewType(BaseViewType):
        def __init__(self):
            self.model = model
            self.fields = list(getAllFields(model))
            self.success_url = success
            self.template_name = self.getTemplatePath()

        def getTemplateDir(self, model):
            dirName = f"{model.__name__[0].lower()}{model.__name__[1:]}/"
            dirName = dirName if os.path.isfile(f"{os.getcwd()}/MainApp/templates/{dirName}/{operationName}.html") else ""
            return dirName if os.path.isdir(f"{os.getcwd()}/MainApp/templates/{dirName}") else ""

        def getTemplatePath(self):
            return f"{self.getTemplateDir(self.model)}{operationName}.html"

    return CreatedViewType


class CRUDBinder():
    def __init__(self, model):
        self.model = model

        self.CreateViewType = createViewType(model, CreateView, "create")
        self.ReadViewType   = createViewType(model, ListView,   "read")
        self.UpdateViewType = createViewType(model, UpdateView, "update")
        self.DeleteViewType = createViewType(model, DeleteView, "delete")


def createCRUDBinder(model: models.Model):
    class CreatedCRUDBinder(CRUDBinder):
        pass
    return CreatedCRUDBinder(model)
