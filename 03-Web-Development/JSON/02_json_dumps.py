import json


university_payload = {
    "university_name": "HNGU",
    "campus_code": 102,
    "is_accredited": True,
    "funding_grant": None,
    "departments": ["Computer Application", "Information Technology"],
    "semester_data": {
        "semester": 4,
        "total_students": 120,
        "subject_credits": {
            "Python": 4,
            "Web_Development": 3,
            "Database_Management": 4
        }
    },
    "top_students": [
        {
            "roll_no": 3,
            "name": "Akash Raval",
            "cpa": 9.2,
            "is_active": True,
            "backlog_subjects": None,
            "skills": ["Python", "Flask", "MySQL", "JavaScript"]
        },
        {
            "roll_no": 7,
            "name": "Rohan Patel",
            "cpa": 8.7,
            "is_active": False,
            "backlog_subjects": ["C++"],
            "skills": ["HTML", "CSS"]
        }
    ]
}


json_string = json.dumps(university_payload)


print("--- OUTPUT JSON STRING ---")
print(json_string)

print("\n--- TYPE CHECK ---")
print("Python Data Type:", type(json_string))
