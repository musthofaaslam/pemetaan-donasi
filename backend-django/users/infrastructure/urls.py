# accounts/presentation/urls.py atau accounts/urls.py

from django.urls import path
# Impor Views yang sudah kita buat sebelumnya
from users.infrastructure.views import RegisterInstitutionView #RequestDonorOTPView

# Tentukan app_name untuk namespace (opsional tapi praktik yang baik)
app_name = 'users'

urlpatterns = [
    # Jalur untuk Registrasi Instansi
    path('institutions/register/', RegisterInstitutionView.as_view(), name='register_institution'),
    
    # # Jalur untuk Permintaan OTP Donor
    # path('donors/request-otp/', RequestDonorOTPView.as_view(), name='request_donor_otp'),
]