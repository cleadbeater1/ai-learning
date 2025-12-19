from ingestion.load_csv import load_technicians_from_csv
from analytics.repeat_analysis import print_repeat_report

def main() -> None:
    technicians = load_technicians_from_csv("data/raw/technicians_raw.csv")
    print_repeat_report(technicians, threshold = 0.15)

if __name__ == "__main__":
    main()