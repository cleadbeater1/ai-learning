import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "raw", "technicians_raw.csv")

technicians = []

with open(csv_path, newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            name = row["name"]

            if name == "":
                raise ValueError("Missing name")

            jobs = int(row["jobs_completed"])
            repeat = int(row["repeat_jobs"]) if row["repeat_jobs"] else 0

            technicians.append({
                "name": name,
                "jobs_completed": jobs,
                "repeat_jobs": repeat
            })

        except ValueError as e:
            print("Skipping row:", row, "| Reason:", e)

for tech in technicians:
    jobs = tech["jobs_completed"]
    repeat = tech["repeat_jobs"]

    if jobs == 0:
        repeat_rate = 0
    else: 
        repeat_rate = repeat / jobs
    
    risk = "! HIGH RISK !" if repeat_rate > 0.2 else ""

    print(
        tech["name"], 
        "repeat rate:", 
        round(repeat_rate, 2),
        risk
    )

print("\nSummary")
print("Technicians analyzed:", len(technicians))

total_jobs = sum(t["jobs_completed"] for t in technicians)
print("Totatl jobs proccessed:", total_jobs)
