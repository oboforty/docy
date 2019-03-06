from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse


def landing(request: HttpRequest):
  """
  Landing page index
  """

  return render(request, 'landing.html', {

  })




