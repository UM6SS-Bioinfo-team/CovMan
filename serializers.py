from ..models import *
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
class VirusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virus
        fields = '__all__'
class ACESerializer(serializers.ModelSerializer):
    class Meta:
        model = ACE
        fields = '__all__'
class VirusVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virus_var
        fields = '__all__'
class ACEVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACE_Var
        fields = '__all__'