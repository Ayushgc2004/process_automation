import json

def generate_report(stats, crm_success, crm_fail, email_success, email_fail):
    report = {
        "Total Raw Leads": stats["total_raw"],
        "Duplicates Removed": stats["duplicates_removed"],
        "Leads Skipped": stats["skipped_missing_email"],
        "Final Processed Leads": stats["final_cleaned"],
        "Successful CRM Updates": crm_success,
        "Failed CRM Updates": crm_fail,
        "Emails Sent": email_success,
        "Email Failures": email_fail
    }

    with open("reports/summary_report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report