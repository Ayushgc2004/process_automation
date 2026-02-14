## Architecture
Pure Python Modular Pipeline

## Why This Architecture?
- Lightweight
- Easy to maintain
- No unnecessary orchestration overhead
- Easily scalable to Airflow or Celery later
- Cron-compatible

## Execution Flow
1. Data Cleanup
2. CRM Integration
3. Email Trigger (only after CRM success)
4. Report Generation

## How to Run

pip install -r requirements.txt
python src/main.py

## Failure Handling
- Each lead processed independently
- CRM failures do not stop pipeline
- Email sent only after CRM success
- All failures logged in report

## Scalability Improvements
- Replace mock CRM with real REST API
- Use async requests for faster processing
- Add retry mechanism
- Add logging framework
- Add Docker container
- Deploy via cron or Airflow
- Add database storage
