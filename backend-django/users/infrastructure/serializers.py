from rest_framework import serializers

class RegisterInstitutionSerializer(serializers.Serializer):
    # Serializer bertugas ketat mengecek sintaksis / format data dari HTTP Request
    name = serializers.CharField(max_length=150, error_messages={"required": "Nama institusi wajib diisi."})
    password = serializers.CharField(max_length=128, write_only=True, error_messages={"required": "Password wajib diisi."})
    email = serializers.EmailField(error_messages={"invalid": "Format email tidak valid."})
    legal_sk_number = serializers.CharField(max_length=100)
    npwp = serializers.CharField(max_length=20)
    pub_permit_no = serializers.CharField(max_length=100)
    bank_account_no = serializers.CharField(max_length=30)
    bank_name = serializers.CharField(max_length=50)
    bank_account_name = serializers.CharField(max_length=150)
    
class LoginInstitutionSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages={"invalid": "Format email tidak valid."})
    password = serializers.CharField(write_only=True)

# class RequestOTPSerializer(serializers.Serializer):
#     # Memastikan input nomor HP dan email dari donor berformat benar
#     phone_number = serializers.CharField(max_length=15)
#     email = serializers.EmailField()

#     def validate_phone_number(self, value):
#         # Anda bisa menambahkan validasi format tambahan di sini jika perlu, 
#         # misalnya harus diawali '08' atau '+62'
#         if not value.startswith(('08', '+62')):
#             raise serializers.ValidationError("Nomor telepon harus diawali dengan 08 atau +62.")
#         return value