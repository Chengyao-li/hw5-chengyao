import sys
import pandas as pd


def audit_csv(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error: Could not read the CSV file. Details: {e}")
        return

    print("CSV QUALITY AUDIT REPORT")
    print("=" * 30)

    print(f"\nDataset shape: {df.shape[0]} rows and {df.shape[1]} columns")

    print("\nColumn data types:")
    print(df.dtypes)

    print("\nMissing values by column:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("No missing values found.")

    print("\nDuplicate rows:")
    duplicate_count = df.duplicated().sum()
    print(duplicate_count)

    print("\nEmpty columns:")
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    if empty_cols:
        print(empty_cols)
    else:
        print("No completely empty columns found.")

    print("\nBasic recommendations:")
    if missing.sum() > 0:
        print("- Review columns with missing values before analysis.")
    if duplicate_count > 0:
        print("- Consider removing or investigating duplicate rows.")
    if empty_cols:
        print("- Remove completely empty columns.")
    if missing.sum() == 0 and duplicate_count == 0 and not empty_cols:
        print("- No major basic data quality issues were detected.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audit_csv.py path/to/file.csv")
    else:
        audit_csv(sys.argv[1])