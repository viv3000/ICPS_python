from django.urls import path
from django.urls import include

from .viewsGenerator import createView, BindedUpdate, BindedDelete, BindedRead, CRUDBinderICPS

def includeCRUD(model):
    binder = createBind(model)
    urls = [
        #path("create", BindedCreate.as_view(BindedCreate, binder)),
        path("create", createView(binder)),
        path("read",   BindedRead.as_view(BindedRead, binder)),
        path("update", BindedUpdate.as_view(binder)),
        path("delete", BindedDelete.as_view(binder)),
    ]
    return include(urls)
