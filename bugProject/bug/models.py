from django.db import models

# Create your models here.

class bugModel(models.Model):
    bugTypeChoices = [
        ("err", "Error"),
        ("feature", "New Feature"),
        ("enhancement", "Enhancement"),
        ("security", "Security Issue"),
        ("performance", "Performance Issue"),
        ("design", "Design Issue"),
        ("documentation", "Documentation Issue"),
    ]
    statusChoices = [
        ("to_do", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("on_hold", "On Hold"),
        ("invalid", "Invalid"),
        ("duplicate", "Duplicate"),
        ("wontfix", "Won't Fix"),
    ]
    description: models.TextField()
    bug_type: models.CharField(max_length=15, choices=bugTypeChoices)
    report_date: models.DateField()
    status: models.CharField(max_length=15, choices=statusChoices)

