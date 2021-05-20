from django.shortcuts import render

# Create your views here.
import json
from datetime import datetime
from django.http import HttpResponse, JsonResponse
import math

def add(request, *args, **kwargs):
    cif = request.body
    if cif:
            cif1 = json.loads(cif)
            try:
                cif1['A'] = int(cif1['A'])
                cif1['B'] = int(cif1['B'])
                summ = cif1['A'] + cif1['B']
                response_data = {
                    'answer': str(summ),
                }
                response = JsonResponse(response_data)
            except:
                response_data = {
                    'answer': 'Enter only whole numbers!!'
                }
                response = JsonResponse(response_data)
                response.status_code = 400
    else:
        response_data = {
            'answer': 'Not Json!!'
        }
        response = JsonResponse(response_data)
        response.status_code = 400

    return response



def subtract(request, *args, **kwargs):
    cif = request.body
    if cif:
            cif1 = json.loads(cif)
            try:
                cif1['A'] = int(cif1['A'])
                cif1['B'] = int(cif1['B'])
                subtract = cif1['A'] - cif1['B']
                response_data = {
                    'answer': str(subtract),
                }
                response = JsonResponse(response_data)
            except:
                response_data = {
                    'answer': 'Enter only whole numbers!!'
                }
                response = JsonResponse(response_data)
                response.status_code = 400
    else:
        response_data = {
            'answer': 'Not Json!!'
        }
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


def multiply(request, *args, **kwargs):
    cif = request.body
    if cif:
            cif1 = json.loads(cif)
            try:
                cif1['A'] = int(cif1['A'])
                cif1['B'] = int(cif1['B'])
                multiply = cif1['A'] * cif1['B']
                response_data = {
                    'answer': str(multiply),
                }
                response = JsonResponse(response_data)
            except:
                response_data = {
                    'answer': 'Enter only whole numbers!!'
                }
                response = JsonResponse(response_data)
                response.status_code = 400
    else:
        response_data = {
            'answer': 'Not Json!!'
        }
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


def divide(request, *args, **kwargs):
    cif = request.body
    if cif:
            cif1 = json.loads(cif)
            try:
                cif1['A'] = int(cif1['A'])
                cif1['B'] = int(cif1['B'])
                if cif1['B'] == 0:
                    response_data = {
                        'answer': 'Division by zero!!!'
                    }
                    response = JsonResponse(response_data)
                    response.status_code = 400
                else:
                    divide = cif1['A'] / cif1['B']
                    response_data = {
                        'answer': str(divide),
                    }
                    response = JsonResponse(response_data)
            except:
                response_data = {
                    'answer': 'Enter only whole numbers!!'
                }
                response = JsonResponse(response_data)
                response.status_code = 400
    else:
        response_data = {
            'answer': 'Not Json!!'
        }
        response = JsonResponse(response_data)
        response.status_code = 400
    return response


