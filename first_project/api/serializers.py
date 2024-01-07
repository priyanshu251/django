from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField() # for id to be visible
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



#  to make forms in django
# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     roll = forms.IntegerField()
#     city = forms.CharField(max_length=100)