def send_email(lead):
    try:
        print(f"Sending email to {lead['Email']}")
        return True
    except Exception:
        return False