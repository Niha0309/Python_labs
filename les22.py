#dictionary
user = {
    "Name": "Fahima Lokman Niha",
    "Age": 22,
    "Email": "nihafahima5@gmail.com",
    "is_Verified": True
}
print(user)
print(user["Name"])
print(user["Age"])


user["Age"] = 29
print(user.get("Age"))