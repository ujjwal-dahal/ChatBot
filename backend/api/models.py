from django.db import models

class CompanyInformation(models.Model):
    user_name = models.CharField(max_length=255)  
    company_name = models.CharField(max_length=255)  
    location = models.CharField(max_length=255)  
    founded_year = models.IntegerField()  
    about_company = models.TextField()  
    product_and_services = models.TextField()  
    greeting_message = models.TextField()  
    thanks_message = models.TextField()
    epoch = models.IntegerField(default=1000, null=True, blank=True)


    def __str__(self):
        return self.company_name  
