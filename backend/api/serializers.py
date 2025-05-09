
from rest_framework import serializers
from .models import CompanyInformation


class CompanyInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = CompanyInformation
    fields = "__all__"
    
    