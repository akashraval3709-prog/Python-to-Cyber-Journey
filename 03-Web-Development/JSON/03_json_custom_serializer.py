import json
from datetime import date

employee = {
    "name": "Akash",
    "joining_date": date(2026, 4, 1) 

}


def custom_serializer(obj):
    if isinstance(obj , date):
        return obj.isoformat();
    raise TypeError(f"TypeError: Object of type datetime is not JSON serializable")


json_string = json.dumps(employee,default=custom_serializer)

print(json_string)
