from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="general")
    urgency = models.IntegerField(default=1)
    severity = models.IntegerField(default=1)
    people_affected = models.IntegerField(default=1)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return self.title


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.volunteer.name} -> {self.report.title}"