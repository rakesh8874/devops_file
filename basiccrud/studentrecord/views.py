from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializer import StudentSerializer


# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
