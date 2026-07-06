from datetime import datetime, timezone
from typing import Optional
from users.domain.entities import InstitutionEntity #DonorEntity
from users.domain.exceptions import InstitutionAlreadyExistException #OTPSpamException
from users.domain.repositories import InstitutionRepositoryInterface #DonorRepositoryInterface
from django.contrib.auth.hashers import make_password

class RegisterInstitutionUseCase:
    def __init__(self, institution_repo: InstitutionRepositoryInterface):
        # Kita panggil interfacenya, bukan class Django-nya langsung
        self.institution_repo = institution_repo

    def execute(self, name: str, email: str, password: str, legal_sk_number: str, npwp: str, 
                pub_permit_no: str, bank_account_no: str, bank_name: str, 
                bank_account_name: str) -> InstitutionEntity:
        
        # 1. Aturan Bisnis: Cek apakah email sudah terdaftar
        if self.institution_repo.get_by_email(email):
            raise InstitutionAlreadyExistException(f"Email {email} sudah digunakan oleh institusi lain.")
            
        # 2. Aturan Bisnis: Cek apakah nama institusi sudah terdaftar (Pemerataan & Validitas)
        if self.institution_repo.get_by_name(name):
            raise InstitutionAlreadyExistException(f"Nama institusi '{name}' sudah terdaftar.")

        # 3. Hash password default untuk institusi baru (misal: "defaultpassword123")
        hashed_password = make_password(password)

        # 3. Buat entitas baru dengan status default 'pending'
        new_institution = InstitutionEntity(
            id=None,
            name=name,
            password=hashed_password,
            email=email,
            legal_sk_number=legal_sk_number,
            npwp=npwp,
            pub_permit_no=pub_permit_no,
            bank_account_no=bank_account_no,
            bank_name=bank_name,
            bank_account_name=bank_account_name,
            verification_status='pending',
            is_frozen=False,
            created_at=None # Nanti di-handle otomatis oleh database
        )

        # 4. Simpan melalui repo kontrak, dan kembalikan entitas hasilnya
        return self.institution_repo.save(new_institution)


# class RequestDonorOTPUseCase:
#     def __init__(self, donor_repo: DonorRepositoryInterface):
#         self.donor_repo = donor_repo

#     def execute(self, phone_number: str, email: str) -> DonorEntity:
#         # 1. Cari dulu apakah donor sudah ada di sistem
#         donor = self.donor_repo.get_by_phone(phone_number)

#         if donor:
#             # 2. Aturan Bisnis Real-time: Cek apakah donor spamming OTP (Fungsi murni dari Entity)
#             if donor.is_spamming_otp():
#                 raise OTPSpamException("Mohon tunggu 1 menit sebelum meminta kode OTP kembali.")
            
#             # Update waktu kirim OTP terakhir
#             donor.last_otp_sent_at = datetime.now(timezone.utc)
#         else:
#             # Jika donor baru pertama kali masuk, daftarkan otomatis
#             donor = DonorEntity(
#                 id=None,
#                 phone_number=phone_number,
#                 email=email,
#                 is_blacklisted=False,
#                 last_otp_sent_at=datetime.now(timezone.utc)
#             )

#         # 3. Simpan state donor terbaru ke database
#         saved_donor = self.donor_repo.save(donor)
        
#         # 4. INFO: Proses pengiriman SMS/WhatsApp OTP yang sebenarnya 
#         # dipicu di sini (bisa lewat Third-Party Service Adapter di Infrastructure)
        
#         return saved_donor