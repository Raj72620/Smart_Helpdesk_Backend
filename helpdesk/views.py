from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
from rest_framework import viewsets, permissions
from .models import Ticket
from .serializers import TicketSerializer
from .utils import classify_ticket

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]  # 🔒 Only logged-in users

    def perform_create(self, serializer):
        description = self.request.data.get("description", "")
        category, assigned_team, solution = classify_ticket(description)

        ticket = serializer.save(
            created_by=self.request.user,
            category=category,
            assigned_team=assigned_team
        )

        if solution:
            ticket.status = "resolved"
            ticket.solution = solution
            ticket.save()