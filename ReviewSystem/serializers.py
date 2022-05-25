from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

    def validate_name(self, value):
        if len(value) < 2:
            return serializers.ValidationError('please enter proper name')
        return value.lower()
    def validate_previous_company(self, value):
        if len(value) < 3:
            return serializers.ValidationError('please enter proper company name')
        return value.lower()
    def validate_college_name(self, value):
        if len(value) < 3:
            return serializers.ValidationError('please enter proper college name')
        return value.lower()


