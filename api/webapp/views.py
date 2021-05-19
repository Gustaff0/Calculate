from django.shortcuts import render

# Create your views here.
import json
from datetime import datetime
from django.http import HttpResponse
import math

def add(request, *args, **kwargs):
    cif = json.loads(request.body)
    if cif:
        if cif['A'] and cif['B']:
            summ = cif['A'] + cif['B']
            response_data = {
                'result': str(summ),
                'method': request.method,
            }
    response = HttpResponse(json.dumps(response_data))
    response['Content_Type'] = 'application/json'
    return response


def subtract(request, *args, **kwargs):
    cif = json.loads(request.body)
    if cif:
        if cif['A'] and cif['B']:
            subtract = cif['A'] - cif['B']
            response_data = {
                'result': str(subtract),
                'method': request.method,
            }
    response = HttpResponse(json.dumps(response_data))
    response['Content_Type'] = 'application/json'
    return response


def multiply(request, *args, **kwargs):
    cif = json.loads(request.body)
    if cif:
        if cif['A'] and cif['B']:
            multiply = cif['A'] * cif['B']
            response_data = {
                'result': str(multiply),
                'method': request.method,
            }
    response = HttpResponse(json.dumps(response_data))
    response['Content_Type'] = 'application/json'
    return response


def divide(request, *args, **kwargs):
    cif = json.loads(request.body)
    if cif:
        if cif['A'] and cif['B']:
            divide = cif['A'] / cif['B']
            response_data = {
                'result': str(divide),
                'method': request.method,
            }
    response = HttpResponse(json.dumps(response_data))
    response['Content_Type'] = 'application/json'
    return response
