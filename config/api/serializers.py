from rest_framework import serializers
from .models import Report, Volunteer, Assignment


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"


class AssignmentSerializer(serializers.ModelSerializer):
    report_title = serializers.CharField(source="report.title", read_only=True)
    volunteer_name = serializers.CharField(source="volunteer.name", read_only=True)

    class Meta:
        model = Assignment
        fields = "__all__"