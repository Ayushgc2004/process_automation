import random

def send_to_crm(lead):
    try:
        # Simulate random failure
        if random.choice([True, False, True]):
            return True
        else:
            raise Exception("CRM API failed")
    except Exception:
        return False