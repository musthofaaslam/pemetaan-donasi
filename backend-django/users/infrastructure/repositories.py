from typing import Optional
from users.domain.repositories import InstitutionRepositoryInterface #DonorRepositoryInterface
from users.domain.entities import InstitutionEntity #DonorEntity
from users.infrastructure.models import DjangoInstitutionModel #DjangoDonorModel
from users.infrastructure.mappers import InstitutionMapper #DonorMapper

class DjangoInstitutionRepository(InstitutionRepositoryInterface):
    
    def save(self, institution: InstitutionEntity) -> InstitutionEntity:
        # 1. Ubah Entity menjadi Django Model menggunakan Mapper
        model_instance = InstitutionMapper.to_model(institution)
        
        # 2. Simpan ke PostgreSQL menggunakan ORM Django (.save())
        # update_or_create digunakan agar fungsi ini bisa untuk Insert baru maupun Update data lama
        model_instance.save()
        
        # 3. Kembalikan lagi dalam bentuk Entity ke Use Case
        return InstitutionMapper.to_entity(model_instance)

    def get_by_email(self, email: str) -> Optional[InstitutionEntity]:
        # Menggunakan ORM Django untuk query berdasarkan email
        model_instance = DjangoInstitutionModel.objects.filter(email=email).first()
        if model_instance:
            return InstitutionMapper.to_entity(model_instance)
        return None

    def get_by_name(self, name: str) -> Optional[InstitutionEntity]:
        # Menggunakan ORM Django untuk query berdasarkan nama (case-insensitive __iexact opsional)
        model_instance = DjangoInstitutionModel.objects.filter(name__iexact=name).first()
        if model_instance:
            return InstitutionMapper.to_entity(model_instance)
        return None


# class DjangoDonorRepository(DonorRepositoryInterface):
    
#     def save(self, donor: DonorEntity) -> DonorEntity:
#         model_instance = DonorMapper.to_model(donor)
#         model_instance.save()
#         return DonorMapper.to_entity(model_instance)

#     def get_by_phone(self, phone_number: str) -> Optional[DonorEntity]:
#         model_instance = DjangoDonorModel.objects.filter(phone_number=phone_number).first()
#         if model_instance:
#             return DonorMapper.to_entity(model_instance)
#         return None

#     def get_by_email(self, email: str) -> Optional[DonorEntity]:
#         model_instance = DjangoDonorModel.objects.filter(email=email).first()
#         if model_instance:
#             return DonorMapper.to_entity(model_instance)
#         return None