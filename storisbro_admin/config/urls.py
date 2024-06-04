"""
URL configuration for storisbro_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from creatives_admin.views import CheckAllAdminCreativesListAPIView, CheckCreativesAPIView
from communities_admin.views import CheckAllAdminCommunitiesListAPIView, CheckCommunityAPIView
# from user_warnings.views import GetUserAPIView, WarningToUserAPIView, GetUserListAPIView, CustomUserAPIView, PK_CustomUserAPIView
from notifications.views import AutoNotificationModelAPIView, PK_AutoNotificationModelAPIView
from ad_links.views import AdLinkModelAPIView, AdLinkClickView
from backup.views import CreateZIPScript, GetZIPDataBase
from reservations_admin.views import GetReservationAPIView
from change.views import ChangeSettingsAPIView, ChangeSettingsAPIViewPK
from notification.views import NotificationToUserAPIView

from django_otp.admin import OTPAdminSite

class OTPAdmin(OTPAdminSite):
    pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dadmin/', admin.site.urls),
    path('api/all_creatives', CheckAllAdminCreativesListAPIView.as_view()),
    path('api/send_notification/<str:message_to_user>/<str:message_to_vk>/<str:message_to_email>/', NotificationToUserAPIView.as_view()),
    # path('api/send_notification/all/<str:message_to_user>/<str:message_to_vk>/<str:message_to_email>/', NotificationToUserAPIView.as_view()),
    path('api/check_creative/<str:type_creative>/<int:pk>', CheckCreativesAPIView.as_view()),
    path('api/cm', CheckAllAdminCommunitiesListAPIView.as_view()),
    path('api/cm/<int:pk>', CheckCommunityAPIView.as_view()),
    path('api/settings_site', ChangeSettingsAPIView.as_view()),
    path('api/settings_site/<int:pk>', ChangeSettingsAPIViewPK.as_view()),
    path('api/n', AutoNotificationModelAPIView.as_view()),
    path('api/n/<int:pk>', PK_AutoNotificationModelAPIView.as_view()),
    path('api/ad_links', AdLinkModelAPIView.as_view()),
    path('api/ad-links/<str:link>', AdLinkClickView.as_view()),
    path('api/z', CreateZIPScript.as_view()),
    path('api/db', GetZIPDataBase.as_view()),
    path('api/reservations/<int:pk>', GetReservationAPIView.as_view())
]
