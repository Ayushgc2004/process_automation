import pandas as pd

def clean_data(input_path, output_path):
    stats = {
        "total_raw": 0,
        "duplicates_removed": 0,
        "skipped_missing_email": 0,
        "final_cleaned": 0
    }

    df = pd.read_excel(input_path)
    stats["total_raw"] = len(df)

    # Trim spaces
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Remove rows with missing email
    before = len(df)
    df = df.dropna(subset=["Email"])
    stats["skipped_missing_email"] = before - len(df)

    # Remove duplicates based on email
    before = len(df)
    df = df.drop_duplicates(subset=["Email"])
    stats["duplicates_removed"] = before - len(df)

    stats["final_cleaned"] = len(df)

    df.to_excel(output_path, index=False)

    return df, stats