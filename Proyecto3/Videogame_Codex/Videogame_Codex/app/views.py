"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Game
from app.forms import GameForm
from django.http import HttpResponseRedirect

def home(request):
    games = Game.objects.order_by('name')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Index',
            'year':datetime.now().year,
            'games' : games
        }
    )

def see_game(request, id):
    game = Game.objects.get(pk = id)
    return render(
        request,
        'app/see_game.html',
        { 'game' : game }
        )

def add_game(request):
    if request.method == 'POST':
        # Formulario rellenado, guardarlo
        formulario = GameForm(request.POST)
        if formulario.is_valid():
        # Guardamos el formulario
            game=formulario.save()
            return HttpResponseRedirect('/game/' + str(game.id))
    elif request.method == 'GET':
        # Peticion de formulario, mandar uno
        # Crear formulario
        formulario = GameForm()
        # Renderizar formulario
        return render(
            request,
            'app/theform.html',
            { 'form' : formulario, 'action' : '/add' }
            )

def delete_game(request, id):
    game = Game.objects.get(pk = id)
    game.delete()
    return HttpResponseRedirect('/')

def edit_game(request,id):
    game = Game.objects.get(pk = id)

    if request.method == 'POST':
        # Formulario rellenado, guardarlo
        formulario = GameForm(request.POST, instance = game)
        if formulario.is_valid():
        # Guardamos el formulario
            game=formulario.save()
            return HttpResponseRedirect('/game/' + str(game.id))
    elif request.method == 'GET':
        # Peticion de formulario, mandar uno
        # Crear formulario
        formulario = GameForm(instance = game)
        # Renderizar formulario
        return render(
            request,
            'app/theform.html',
            { 'form' : formulario, 'action' : '/edit/' + str(game.id)}
            )

def ranking(request):
    games = Game.objects.order_by('-score')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/ranking.html',
        {
            'title':'Ranking',
            'year':datetime.now().year,
            'games' : games
        }
    )