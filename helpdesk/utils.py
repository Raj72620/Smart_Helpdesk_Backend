def classify_ticket(description):
	"""
	Simple rule-based ticket classifier
	Returns:
	- category
	- assigned_team
	- auto_solution (optional)
	"""
	desc = description.lower()
    
	if "password" in desc:
		return "Authentication", "Access Management Team", "Reset your password via SSO portal."
	elif "vpn" in desc:
		return "Network", "Network Team", "Check VPN client settings."
	elif "email" in desc:
		return "Email", "Messaging Team", None
	else:
		return "General", "IT Support", None
