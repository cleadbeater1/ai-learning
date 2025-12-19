import csv
import os

def load_technicians_from_csv(relative_csv_path: str) -> list[dict]:
    """
    Load technician records from a CSV file and return a list of clean dictionaries. 
    -Skip rows with missing nam
    -Converts numeric fields to integers
    -Defaults missint repeat_jobs to 0
    """

    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(base_dir) #go up from /ingestion to project root
    csv_path = os.path.join(project_root, relative_csv_path)

    technicians: list[dict] = []

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                name = row["name"].strip()
                if name == "":
                    raise ValueError("Missing Name")

                jobs = int(row["jobs_completed"])
                repeat = int(row["repeat_jobs"]) if row["repeat_jobs"] else 0

                technicians.append({
                    "name": name,
                    "jobs_completed": jobs,
                    "repeat_jobs": repeat
                })
            except ValueError as e:
                print("Skipping row:", row, "|Reason:", e)
    return technicians