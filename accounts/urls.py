from django.urls import include, path
from rest_framework import routers

from .views import (
    CreateAccount,
    CustomerViewset,
    DriverViewset,
    MyUserPasswordChange,
    MyUserViewset,
    SendOTP,
)

router = routers.DefaultRouter()
router.register(r"customers", CustomerViewset)
router.register(r"drivers", DriverViewset)
router.register(r"users", MyUserViewset)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("user/changepassword/", MyUserPasswordChange.as_view()),
    path("sendotp/", SendOTP.as_view()),
    path("update-account/", CreateAccount.as_view()),
    path("", include(router.urls)),
]
