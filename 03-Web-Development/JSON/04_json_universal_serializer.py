import json
from datetime import datetime


def universal_serializer(obj):
    if isinstance(obj,datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    if isinstance(obj,bytes):
        return obj.decode('utf-8')
    if isinstance(obj,Student):
        return obj.__dict__
    if isinstance(obj,set):
        return list(obj)
    raise TypeError(f"TypeError: Object of {type(obj).__name__} is not JSON serializable")

class Student:
    def __init__(self,name,rollno):
        self.name =name
        self.rollno = rollno


Student_obj = Student("Akash",3)
complex_data = {
    "time": datetime.now(),
    "raw": b"Bytes data",
    "unique_ids": {101, 102, 103},
    "Student-data" : Student_obj

}

json_str = json.dumps(complex_data,indent=2,default=universal_serializer)

print(json_str)

