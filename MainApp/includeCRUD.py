from django.urls import path
from django.urls import include
from django.views.generic.base import RedirectView

from .viewsGenerator import createCRUDBinder

def includeCRUD(model):
    binder = createCRUDBinder(model)
    urls = [
        path("create/", binder.CreateViewType.as_view()),
        path("create",  view=RedirectView.as_view(url="create/", permanent=False)),

        path("read/", binder.ReadViewType.as_view()),
        path("read",  view=RedirectView.as_view(url="read/", permanent=False)),

        path("<pk>/update/", binder.UpdateViewType.as_view()),
        path("<pk>/update",  view=RedirectView.as_view(url="update/", permanent=False)),

        path("<pk>/delete/", binder.DeleteViewType.as_view()),
        path("<pk>/delete",  view=RedirectView.as_view(url="delete/", permanent=False)),
    ]
    return include(urls)
