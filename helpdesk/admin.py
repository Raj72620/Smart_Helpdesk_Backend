from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status', 'assigned_team', 'created_by', 'created_at')
    list_filter = ('status', 'category', 'assigned_team')
    search_fields = ('title', 'description', 'created_by__username')
# Register your models here.
