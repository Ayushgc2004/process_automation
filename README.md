# Process Automation -- Lead Pipeline

## Overview

This project automates daily sales lead processing using Python. It
cleans Excel data, sends leads to a mock CRM, triggers welcome emails
after successful CRM updates, and generates a summary report.

------------------------------------------------------------------------

## Architecture

Modular Python-based pipeline:

Excel Input ↓ Data Cleaning ↓ CRM Integration ↓ Email Automation ↓
Reporting

Each module is separated for maintainability and scalability.

------------------------------------------------------------------------

## Execution Flow

1.  Read `leads.xlsx`
2.  Remove duplicates (Email as unique key)
3.  Skip missing emails
4.  Save `cleaned_leads.xlsx`
5.  Process each lead:
    -   Send to CRM
    -   If successful → Send Email
6.  Generate summary report (JSON / TXT / HTML)

------------------------------------------------------------------------

## How to Run
pip install -r requirements.txt
python main.py

Outputs: - cleaned_leads.xlsx - summary_report.json -
summary_report.txt - summary_report.html

------------------------------------------------------------------------

## Design Decisions

-   Email used as unique identifier
-   Individual lead processing for fault tolerance
-   CRM → Email execution order enforced
-   Modular structure for scalability

------------------------------------------------------------------------

## Failure Handling

-   Missing emails skipped
-   Duplicates removed
-   CRM failures do not stop pipeline
-   Email sent only after CRM success
-   Final report always generated

------------------------------------------------------------------------

## Scalability Improvements

-   Add logging & retry mechanism
-   Use async processing
-   Integrate with Airflow/cron
-   Dockerize for deployment
-   Replace mock CRM/email with real APIs

------------------------------------------------------------------------

✔ Clean modular design\
✔ Fault-tolerant workflow\
✔ Production-ready structure
