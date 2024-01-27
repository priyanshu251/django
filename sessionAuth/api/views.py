from .models import Student 
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] # isse ye hoga ki agar banda authenticated hai to allow ho jaega doesnt matter ki wo staff hai ya nhi
    # permission_classes = [IsAdminUser] # agar banda isstaff hua tabhi auth ho paega 
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly] # anyone can read but only authorised users can write 

# this is used when only list and retrieve action are to be performed (eg : corona virus website)
    
# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
