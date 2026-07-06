from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Impor dari layer Domain (Use Case & Exceptions)
from users.application.usecases import RegisterInstitutionUseCase #RequestDonorOTPUseCase
from users.domain.exceptions import InstitutionAlreadyExistException #OTPSpamException

# Impor dari layer Infrastructure (Repository Implementation)
from users.infrastructure.repositories import DjangoInstitutionRepository #DjangoDonorRepository

# Impor dari layer Presentation (Serializer)
from .serializers import RegisterInstitutionSerializer #RequestOTPSerializer


class RegisterInstitutionView(APIView):
    def post(self, request):
        # 1. Validasi format request HTTP lewat Serializer
        serializer = RegisterInstitutionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Inisialisasi Repository & Use Case (Dependency Injection)
        institution_repo = DjangoInstitutionRepository()
        use_case = RegisterInstitutionUseCase(institution_repo)
        
        # 3. Eksekusi Use Case dan tangkap Exception dari Domain
        try:
            # Jalankan bisnis logik dengan data yang sudah tervalidasi
            result_entity = use_case.execute(
                name=serializer.validated_data['name'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email'],
                legal_sk_number=serializer.validated_data['legal_sk_number'],
                npwp=serializer.validated_data['npwp'],
                pub_permit_no=serializer.validated_data['pub_permit_no'],
                bank_account_no=serializer.validated_data['bank_account_no'],
                bank_name=serializer.validated_data['bank_name'],
                bank_account_name=serializer.validated_data['bank_account_name']
            )
            
            # 4. Berikan respon sukses jika berhasil
            # Karena result_entity adalah objek Python murni, kita return data dasar
            return Response({
                "message": "Institusi berhasil didaftarkan.",
                "data": {
                    "id": result_entity.id,
                    "name": result_entity.name,
                    "email": result_entity.email,
                    "verification_status": result_entity.verification_status
                }
            }, status=status.HTTP_201_CREATED)
            
        except InstitutionAlreadyExistException as e:
            # Tangkap error aturan bisnis dari domain, ubah jadi HTTP 400
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Jaga-jaga jika ada error sistem/database yang tidak terduga
            return Response({"error": "Terjadi kesalahan pada sistem."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class RequestDonorOTPView(APIView):
#     def post(self, request):
#         # 1. Validasi format request HTTP
#         serializer = RequestOTPSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # 2. Inisialisasi Repository & Use Case
#         donor_repo = DjangoDonorRepository()
#         use_case = RequestDonorOTPUseCase(donor_repo)
        
#         # 3. Eksekusi Use Case
#         try:
#             saved_donor = use_case.execute(
#                 phone_number=serializer.validated_data['phone_number'],
#                 email=serializer.validated_data['email']
#             )
            
#             return Response({
#                 "message": "Kode OTP berhasil dikirimkan.",
#                 "data": {
#                     "phone_number": saved_donor.phone_number,
#                     "last_otp_sent_at": saved_donor.last_otp_sent_at
#                 }
#             }, status=status.HTTP_200_OK)
            
#         except OTPSpamException as e:
#             # Tangkap error throttling real-time dari domain
#             return Response({"error": str(e)}, status=status.HTTP_429_TOO_MANY_REQUESTS)
#         except Exception as e:
#             return Response({"error": "Gagal memproses permintaan OTP."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)