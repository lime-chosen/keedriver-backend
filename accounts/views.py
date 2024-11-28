import calendar
import datetime

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.utils import generate_totp, send_otp

from .models import Customer, Driver, MyUser
from .serializers import (
    CustomerSerializer,
    CustomPasswordChangeSerializer,
    DriverSerializer,
    MyUserSerializer,
    SendOTPRequestSerializer,
)

# Create your views here.


class MyUserViewset(viewsets.ModelViewSet):

    queryset = MyUser.objects.all().order_by("-date_joined")
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_staff", "is_driver", "is_customer"]
    ordering_fields = [
        "created_at",
    ]
    search_fields = ["first_name", "last_name", "phone", "username"]


class MyUserPasswordChange(GenericAPIView):
    queryset = MyUser.objects.all()
    serializer_class = CustomPasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = serializer.validated_data.get("id")
        user = MyUser.objects.get(pk=id)
        user.set_password(serializer.validated_data.get("password"))
        user.save()
        return Response({"detail": "New password has been saved."})


class CustomerViewset(viewsets.ModelViewSet):

    queryset = Customer.objects.all().order_by("-date_joined")
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_active"]
    ordering_fields = [
        "created_at",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "phone",
    ]

    @action(detail=False, methods=["get"], url_path="chart")
    def get_customer_chart(self, request):
        range = request.data.range
        if range == "LAST30":
            pass

        if range == "LAST6":
            pass

        if range == "CUSTOM":
            pass

        today = datetime.date.today()
        year = today.year
        users = Customer.objects.filter(date_joined__year=year)
        months = []
        for user in users:
            months.append(user.date_joined.date().month)
        months = list(set(months))
        months.sort()
        data = []
        for month in months:
            data.append(
                {
                    "month": calendar.month_name[month],
                    "count": Customer.objects.filter(date_joined__month=month).count(),
                }
            )
        return Response(data, status=status.HTTP_200_OK)


class DriverViewset(viewsets.ModelViewSet):

    queryset = Driver.objects.all().order_by("-date_joined")
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["is_active"]
    ordering_fields = [
        "created_at",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "phone",
    ]

    @action(detail=False, methods=["get"], url_path="chart")
    def get_driver_chart(self, request):

        users = Driver.objects.filter(date_joined__year=2023)
        months = []
        for user in users:
            months.append(user.date_joined.date().month)
        months = list(set(months))
        months.sort()
        data = []
        for month in months:
            data.append(
                {
                    "month": calendar.month_name[month],
                    "count": Driver.objects.filter(date_joined__month=month).count(),
                }
            )
        return Response(data, status=status.HTTP_200_OK)


class SendOTP(GenericAPIView):
    serializer_class = SendOTPRequestSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        if not phone:
            return Response({"phone": "This field is required."}, status=400)

        otp, status = send_otp(phone)

        if not status:
            return Response({"detail": "OTP Error. Try again"}, status=400)

        return Response({"detail": "OTP has been sent.", "otp": otp}, status=200)


class CreateAccount(GenericAPIView):
    serializer_class = MyUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user

        if not user:
            return Response({"detail": "User not found."}, status=404)

        email_already_exists = MyUser.objects.filter(
            email=request.data.get("email")
        ).exists()

        if email_already_exists:
            return Response({"detail": "Email already exists."}, status=400)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({"detail": "Account details have been updated."}, status=200)
