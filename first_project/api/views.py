from operator import truediv
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse

# Create your views here.
# creating model object - single student data 

def student_details(request, pk): # what is request here
    stu = Student.objects.get(id = pk) # getting model object (just 1) 
    # print(stu) # this is a complex data or sql queries
    serializer = StudentSerializer(stu) # calling studentserializer class in serilalizers.py and passing the model object that is to be serialized
    # print(serializer)
    # print(serializer.data) # this is a python dictionarym, can be distinguished as parameter on left side are in single quote 
    # json_data = JSONRenderer().render(serializer.data) # rendering the serialized data in json format
    # print(json_data) # this is json format as the same is in double quotes
    # return HttpResponse(json_data,content_type='application/json') # creating a response to be shown in frontend
      



# query set - all student data 
def student_list(request): 
    stu = Student.objects.all() 
    serializer = StudentSerializer(stu, many= truediv)
    return JsonResponse(serializer.data, safe=False) # safe is requiered to be set for non-dict objects, heree student list is a query set
