from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from django.conf import settings
import os

from .models import Report, Volunteer, Assignment
from .serializers import ReportSerializer, VolunteerSerializer, AssignmentSerializer
from matching.priority import get_priority_reports
from matching.matcher import match_volunteers
from rag.chatbot import ask_rag


def home(request):
    path = os.path.join(settings.BASE_DIR.parent, "frontend", "index.html")
    return FileResponse(open(path, "rb"))


def frontend_css(request):
    path = os.path.join(settings.BASE_DIR.parent, "frontend", "style.css")
    return FileResponse(open(path, "rb"), content_type="text/css")


def frontend_js(request):
    path = os.path.join(settings.BASE_DIR.parent, "frontend", "script.js")
    return FileResponse(open(path, "rb"), content_type="application/javascript")


@api_view(["GET", "POST"])
def reports(request):
    if request.method == "POST":
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    data = Report.objects.all()
    return Response(ReportSerializer(data, many=True).data)


@api_view(["GET", "POST"])
def volunteers(request):
    if request.method == "POST":
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    data = Volunteer.objects.all()
    return Response(VolunteerSerializer(data, many=True).data)


@api_view(["GET"])
def priority_tasks(request):
    data = get_priority_reports(Report.objects.all())
    return Response(data)


@api_view(["POST"])
def chatbot(request):
    question = request.data.get("question", "")
    if not question:
        return Response({"error": "question field is required"})
    return Response({"answer": ask_rag(question)})


@api_view(["GET"])
def match_worker(request, report_id):
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return Response({"error": "Report not found"})

    volunteers = Volunteer.objects.all()
    return Response(match_volunteers(report, volunteers))


@api_view(["POST"])
def assign(request):
    report_id = request.data.get("report_id")
    volunteer_id = request.data.get("volunteer_id")

    if not report_id or not volunteer_id:
        return Response({"error": "report_id and volunteer_id are required"})

    try:
        report = Report.objects.get(id=report_id)
        volunteer = Volunteer.objects.get(id=volunteer_id)
    except Report.DoesNotExist:
        return Response({"error": "Report not found"})
    except Volunteer.DoesNotExist:
        return Response({"error": "Volunteer not found"})

    if not volunteer.available:
        return Response({"error": "Volunteer already assigned or not available"})

    assignment = Assignment.objects.create(report=report, volunteer=volunteer)
    volunteer.available = False
    volunteer.save()

    report.status = "assigned"
    report.save()

    return Response({
        "message": f"{volunteer.name} assigned to {report.title}",
        "assignment_id": assignment.id,
        "report_status": report.status
    })


@api_view(["GET"])
def assignments(request):
    data = Assignment.objects.all()
    return Response(AssignmentSerializer(data, many=True).data)


@api_view(["GET"])
def stats(request):
    return Response({
        "total_reports": Report.objects.count(),
        "pending_reports": Report.objects.filter(status="pending").count(),
        "assigned_reports": Report.objects.filter(status="assigned").count(),
        "total_volunteers": Volunteer.objects.count(),
        "available_volunteers": Volunteer.objects.filter(available=True).count(),
        "assigned_volunteers": Volunteer.objects.filter(available=False).count(),
        "total_assignments": Assignment.objects.count()
    })


@api_view(["POST"])
def update_status(request):
    report_id = request.data.get("report_id")
    status = request.data.get("status")

    if not report_id or not status:
        return Response({"error": "report_id and status are required"})

    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return Response({"error": "Report not found"})

    report.status = status
    report.save()

    return Response({
        "message": "Report status updated",
        "report_id": report.id,
        "status": report.status
    })