class InstitutionAlreadyExistException(Exception):
    """Dilemparkan ketika institusi yang sama sudah ada di sistem."""
    pass

class InstitutionFrozenException(Exception):
    """Dilemparkan ketika institusi yang dibekukan mencoba melakukan aksi (misal: menerima donasi)."""
    pass

class InstitutionNotVerifiedException(Exception):
    """Dilemparkan ketika institusi belum diverifikasi oleh admin."""
    pass

class InstitutionInvalidCredentialsException(Exception):
    """Dilemparkan ketika kredensial login institusi tidak valid."""
    pass

# class OTPSpamException(Exception):
#     """Dilemparkan ketika donor meminta OTP terlalu cepat sebelum batas waktu jeda selesai."""
#     pass

# class DonorBlacklistedException(Exception):
#     """Dilemparkan ketika donor yang masuk daftar hitam mencoba masuk ke sistem."""
#     pass