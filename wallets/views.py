from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, permissions, viewsets

from keedriver.permissions import IsDriver

from .models import DriverWallet, DriverWalletTransaction
from .serializers import DriverWalletSerializer, DriverWalletTransactionSerializer

# Create your views here.


@extend_schema(
    tags=["Admin Wallet"],  # Add your custom tag here
)
class AdminDriverWalletViewset(viewsets.ModelViewSet):

    queryset = DriverWallet.objects.all()
    serializer_class = DriverWalletSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["driver__first_name", "driver__phone"]
    search_fields = ["driver__first_name", "driver__phone"]

    class Meta:
        ordering = "-created_at"


@extend_schema(
    tags=["Admin Wallet"],  # Add your custom tag here
)
class AdminDriverWalletTransactionViewset(viewsets.ModelViewSet):

    queryset = DriverWalletTransaction.objects.all()
    serializer_class = DriverWalletTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["wallet__driver__first_name", "wallet__driver__phone"]
    search_fields = ["wallet__driver__first_name", "wallet__driver__phone"]

    class Meta:
        ordering = "-created_at"


@extend_schema(
    tags=["Driver Wallet"],  # Add your custom tag here
)
class DriverWalletViewset(viewsets.ModelViewSet):

    queryset = DriverWallet.objects.all()
    serializer_class = DriverWalletSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriver]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["driver__first_name", "driver__phone"]
    search_fields = ["driver__first_name", "driver__phone"]

    class Meta:
        ordering = "-created_at"

    def get_queryset(self):
        queryset = DriverWallet.objects.filter(driver=self.request.user)
        return queryset


@extend_schema(
    tags=["Driver Wallet"],  # Add your custom tag here
)
class DriverWalletTransactionViewset(viewsets.ModelViewSet):

    queryset = DriverWalletTransaction.objects.all()
    serializer_class = DriverWalletTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDriver]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ["wallet__driver__first_name", "wallet__driver__phone"]
    search_fields = ["wallet__driver__first_name", "wallet__driver__phone"]

    class Meta:
        ordering = "-created_at"

    def get_queryset(self):
        queryset = DriverWalletTransaction.objects.filter(driver=self.request.user)
        return queryset
