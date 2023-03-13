from django.shortcuts import render

from django.views import generic

from .models import Client, Credit, Account


class RenderClient(generic.ListView):
    model = Client
    template_name = "client.html"
    context_object_name = "clients" # По умолчанию object_list


class RenderClientDetail(generic.DetailView):
    model = Client
    template_name = "client_detail.html"
    context_object_name = "client" # По умолчанию object_list