from django.db import models

class DjangoInstitutionModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=128)  
    legal_sk_number = models.CharField(max_length=100)
    npwp = models.CharField(max_length=20)
    pub_permit_no = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=50)
    bank_account_name = models.CharField(max_length=150)
    verification_status = models.CharField(max_length=20, default='pending')
    is_frozen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'institutions'  
        
# class DjangoDonorModel(models.Model):
#     phone_number = models.CharField(max_length=15, unique=True)
#     email = models.EmailField(unique=True, max_length=150)
#     is_blacklisted = models.BooleanField(default=False)
#     last_otp_sent_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         db_table = 'donors'