def compute_repeat_rate(tech: dict) -> float:
    """
    Returns repeat rate = repeat_jobs / jobs_completed, safely
    
    :param tech: Description
    :type tech: dict
    :return: Description
    :rtype: float
    """

    jobs = tech.get("jobs_completed", 0)
    repeat = tech.get("repeat_jobs", 0)

    if jobs == 0: 
        return 0.0
    
    return repeat / jobs

def risk_label(repeat_rate: float, threshold: float = 0.2) -> str:
    """
    Returns a risk label if repeat_rate is above the threshold. 
    
    :param repeat_rate: Description
    :type repeat_rate: float
    :param threshold: Description
    :type threshold: float
    :return: Description
    :rtype: str
    """

    return "! HIGH RISK !" if repeat_rate > threshold else ""

def print_repeat_report(technicians: list[dict], threshold: float = 0.2) -> None:
    """
    Prints a simple technician repeat report. 
    
    :param technicians: Description
    :type technicians: list[dict]
    :param threshold: Description
    :type threshold: float
    """

    print("\nTechnician Repeat Analysis")

    for tech in technicians: 
        rate = compute_repeat_rate(tech)
        label = risk_label(rate, threshold)

        print(
            tech.get("name", "Unknown"),
            "repeat rate:", 
            round(rate, 2), 
            label
        )
    print("\nSummary")
    print("Technicians analyzed:", len(technicians))