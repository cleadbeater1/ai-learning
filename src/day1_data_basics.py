technicians = [
    {"name": "Alex", "jobs_completed": 25, "repeat_jobs": 2},
    {"name": "Jordan", "jobs_completed": 18, "repeat_jobs": 5},
    {"name": "Sam", "jobs_completed": 30, "repeat_jobs": 1},
    {"name": "Chris", "jobs_completed": 22},
    {"name": "Taylor", "jobs_completed": 0, "repeat_jobs": 0}
]



for tech in technicians:
    try:
        repeat = tech["repeat_jobs"]
    except KeyError:
        repeat = 0

    jobs = tech["jobs_completed"]

    #catches divide by zero error, sets rate to zero 
    if jobs == 0:
        repeat_rate = 0
    else: 
        repeat_rate = repeat / jobs

    print(
        tech["name"], 
        "has a repeat rate of ", 
        round(repeat_rate, 2)
    )

