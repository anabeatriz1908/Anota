from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# função que representa a página a ser acessada

def index(request):
    return HttpResponse("Bem-vindo(a) a Agenda Anota Ai")


