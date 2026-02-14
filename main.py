from modules.data_cleaner import clean_data
from modules.crm_integration import send_to_crm
from modules.email_service import send_email
from modules.reporting import generate_report

def main():
    df, stats = clean_data("data/leads.xlsx", "data/cleaned_leads.xlsx")

    crm_success = crm_fail = 0
    email_success = email_fail = 0

    for _, lead in df.iterrows():
        crm_status = send_to_crm(lead)

        if crm_status:
            crm_success += 1
            email_status = send_email(lead)

            if email_status:
                email_success += 1
            else:
                email_fail += 1
        else:
            crm_fail += 1

    generate_report(stats, crm_success, crm_fail, email_success, email_fail)

if __name__ == "__main__":
    main()