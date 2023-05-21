from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly
from .permissions import IsReadOnly, IsGETOrPatch, CustomePermission


class EmpListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class EmpCreteAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class EmpRetriveAPIView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAdminUser, ]


class EmpUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class EmpDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]
