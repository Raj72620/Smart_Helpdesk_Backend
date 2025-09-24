from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)   # for NLP classification later
    urgency = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    assigned_team = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    solution = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
from django.db import models
from django.conf import settings

class Ticket(models.Model):
    # Source of the ticket
    SOURCES = [
        ('chatbot','Chatbot'),
        ('email','Email'),
        ('portal','Portal'),
    ]

    # Status of the ticket
    STATUS = [
        ('open','Open'),
        ('in_progress','In Progress'),
        ('resolved','Resolved'),
    ]

    title = models.CharField(max_length=255)  # Ticket title
    description = models.TextField()          # Detailed description
    category = models.CharField(max_length=100, default="Uncategorized")  # Auto-classified category
    urgency = models.CharField(max_length=20, default="Normal")           # Normal / High / Low
    source = models.CharField(max_length=20, choices=SOURCES, default='chatbot')  # Ticket source
    assigned_team = models.CharField(max_length=100, default="General Support")    # Team handling the ticket
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Who created
    status = models.CharField(max_length=20, choices=STATUS, default="open")  # Ticket status
    solution = models.TextField(blank=True, null=True)                        # Solution if auto-resolved
    created_at = models.DateTimeField(auto_now_add=True)                       # Auto timestamp
