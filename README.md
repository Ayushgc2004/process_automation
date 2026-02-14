# process_automation

This project automates daily sales lead processing using Python.
It cleans Excel data, sends leads to a mock CRM, triggers welcome emails after successful CRM updates, and generates a summary report.

# Execution Flow:
-Read leads.xlsx
-Remove duplicates (Email as unique key)
-Skip missing emails
-Save cleaned_leads.xlsx
-Process each lead:
-Send to CRM
-If successful → Send Email
-Generate summary report (JSON / TXT / HTML)

# How To Run:
pip install -r requirements.txt
python main.py
