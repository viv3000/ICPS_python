from django.shortcuts import render, redirect

def notLoggedUsers(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def getAllFields(model):
    for i in list(model.__dict__.keys()):
        if not (i.count("id") or
                i.count("objects") or
                i.count('DoesNotExist') or
                i.count('MultipleObjectsReturned') or
                i.count("_")):
            yield i


