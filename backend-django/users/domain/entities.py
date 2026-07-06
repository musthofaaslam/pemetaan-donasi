from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class InstitutionEntity:
    id: Optional[int]
    name: str
    password: str
    email: str
    legal_sk_number: str
    npwp: str
    pub_permit_no: str
    bank_account_no: str
    bank_name: str
    bank_account_name: str
    verification_status: str
    is_frozen: bool
    created_at: Optional[datetime]
# @dataclass
# class DonorEntity:
#     id: Optional[int]
#     phone_number: str
#     email: str
#     is_blacklisted: bool
#     last_otp_sent_at: Optional[datetime]