## Architecture
Chosen Approach: Modular Python Pipeline

The system follows a layered modular architecture:

Input (Excel)
     ↓
Data Cleaning Module
     ↓
CRM Integration Module
     ↓
Email Automation Module
     ↓
Reporting Module
     ↓
Output Reports

Folder Structure:
process_automation/
│
├── main.py
├── requirements.txt
│
├── data/
│   ├── leads.xlsx
│   └── cleaned_leads.xlsx
│
├── modules/
│   ├── data_cleaner.py
│   ├── crm_integration.py
│   ├── email_service.py
│   └── reporting.py
│
└── reports/

Why This Architecture?

-Clear separation of concerns

-Easy to test individual modules

-Easy to scale or replace components

-Production-ready structure

-Simple deployment
