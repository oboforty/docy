from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse

"""Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text."""
def landing(request: HttpRequest):
  """
  Landing page index
  """

  return render(request, 'landing.html', {

  })




