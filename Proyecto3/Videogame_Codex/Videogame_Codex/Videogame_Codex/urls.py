"""
Definition of urls for Videogame_Codex.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home),
    url(r'^game\/(?P<id>[0-9]+)$', app.views.see_game),
    url(r'^add\/{0,1}$', app.views.add_game),
    url(r'^delete\/(?P<id>[0-9]+)$', app.views.delete_game),
    url(r'^edit\/(?P<id>[0-9]+)$', app.views.edit_game),
    url(r'^ranking\/$', app.views.ranking),
]
