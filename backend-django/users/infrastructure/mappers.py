from users.domain.entities import InstitutionEntity #DonorEntity
from users.infrastructure.models import DjangoInstitutionModel #DjangoDonorModel

class InstitutionMapper:
    @staticmethod
    def to_entity(model: DjangoInstitutionModel) -> InstitutionEntity:
        return InstitutionEntity(
            id=model.id,
            name=model.name,
            password=model.password,
            email=model.email,
            legal_sk_number=model.legal_sk_number,
            npwp=model.npwp,
            pub_permit_no=model.pub_permit_no,
            bank_account_no=model.bank_account_no,
            bank_name=model.bank_name,
            bank_account_name=model.bank_account_name,
            verification_status=model.verification_status,
            is_frozen=model.is_frozen,
            created_at=model.created_at
        )

    @staticmethod
    def to_model(entity: InstitutionEntity) -> DjangoInstitutionModel:
        # Mengembalikan instance model Django untuk disimpan ke DB
        return DjangoInstitutionModel(
            id=entity.id,
            name=entity.name,
            password=entity.password,
            email=entity.email,
            legal_sk_number=entity.legal_sk_number,
            npwp=entity.npwp,
            pub_permit_no=entity.pub_permit_no,
            bank_account_no=entity.bank_account_no,
            bank_name=entity.bank_name,
            bank_account_name=entity.bank_account_name,
            verification_status=entity.verification_status,
            is_frozen=entity.is_frozen,
            created_at=entity.created_at
        )
        
# class DonorMapper:
#     @staticmethod
#     def to_entity(model: DjangoDonorModel) -> DonorEntity:
#         return DonorEntity(
#             id=model.id,
#             phone_number=model.phone_number,
#             email=model.email,
#             is_blacklisted=model.is_blacklisted,
#             last_otp_sent_at=model.last_otp_sent_at
#         )

#     @staticmethod
#     def to_model(entity: DonorEntity) -> DjangoDonorModel:
#         # Mengembalikan instance model Django untuk disimpan ke DB
#         return DjangoDonorModel(
#             id=entity.id,
#             phone_number=entity.phone_number,
#             email=entity.email,
#             is_blacklisted=entity.is_blacklisted,
#             last_otp_sent_at=entity.last_otp_sent_at
#         )   