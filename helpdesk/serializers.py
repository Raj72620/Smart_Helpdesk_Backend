from rest_framework import serializers
from .models import Ticket  # Adjust the import if your model is elsewhere

class TicketSerializer(serializers.ModelSerializer):
	# Optionally, you can display the username instead of just the ID
	# created_by = serializers.ReadOnlyField(source='created_by.username')

	class Meta:
		model = Ticket
		fields = ['id', 'title', 'description', 'created_by']  # Add other fields as needed
		read_only_fields = ['created_by']  # This makes 'created_by' not required in POST
