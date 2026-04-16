from data_loader import load_csv
from data_cleaner import clean_data
from data_analysis import analyze_data

def main():
    filepath = "data/sample.csv"
    df = load_csv(filepath)
    if df is not None:
        df = clean_data(df)
        analyze_data(df)

if __name__ == "__main__":
    main()
