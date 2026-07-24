import json

raw_api_payload = '''
{
    "user_id": 101,
    "is_active": true,
    "middle_name": null,
    "skills": ["Python", "Flask", "SQL"]
}
'''

# Parsing String to Python Data Structure
user_data = json.loads(raw_api_payload)



print(f"Python Dict:, {user_data}\n")
print(f'is_active Type:, {type(user_data["is_active"])}, "-> Value:", {user_data["is_active"]}\n')
print('middle_name Type:", {type(user_data["middle_name"])}, "-> Value:",{ user_data["middle_name"]}\n')
print("First Skill:", user_data["skills"][0])




