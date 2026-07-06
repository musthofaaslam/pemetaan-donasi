from abc import ABC, abstractmethod
from typing import Optional
from users.domain.entities import InstitutionEntity #DonorEntity

class InstitutionRepositoryInterface(ABC):
    
    @abstractmethod
    def save(self, institution: InstitutionEntity) -> InstitutionEntity:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[InstitutionEntity]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[InstitutionEntity]:
        pass


# class DonorRepositoryInterface(ABC):

#     @abstractmethod
#     def save(self, donor: DonorEntity) -> DonorEntity:
#         pass

#     @abstractmethod
#     def get_by_phone(self, phone_number: str) -> Optional[DonorEntity]:
#         pass

#     @abstractmethod
#     def get_by_email(self, email: str) -> Optional[DonorEntity]:
#         pass