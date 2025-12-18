technician = [
    {"name": "Alex", "jobs_completed": 25, "repeat_jobs": 2},
    {"name": "Jordan", "jobs_completed": 18, "repeat_jobs": 5},
    {"name": "Sam", "jobs_completed": 30, "repeat_jobs": 1},
    {"name": "Chris", "jobs_completed": 22},
    {"name": "John", "jobs_completed": 64, "repeat_jobs": 21}
]

for tech in technician:
    jobs = tech.get("jobs_completed", 0)
    repeat = tech.get("repeat_jobs", 0)

    if jobs == 0:
        repeat_rate = 0
    else:
        repeat_rate = repeat / jobs

    if repeat_rate > 0.15:
        risk = " !HIGH RISK! "
    else:
        risk = ""
    
    print(
        tech["name"], 
        "has completed", jobs,
        "jobs and has a repeat rate of",
        round(repeat_rate, 2),
        risk
    )

