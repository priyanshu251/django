from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import JsonResponse
import json
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        print('first print')
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        print('second print')
        serializer = StudentSerializer(data=python_data)  
        if serializer.is_valid():
            serializer.save() # this line will successfully create a model instance hence a row will be added in table
            response = {'msg' : 'Data created'}
            return JsonResponse(response)
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')

