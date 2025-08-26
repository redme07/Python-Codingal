student = {
    "id1": {
        "name": "Tom",
        "class": "VII",
        "subjects": ["english, math, biology"],
    },
    "id2": {
        "name": "Tom",
        "class": "VII",
        "subjects": ["english, math, biology"],
    },
    "id3": {
        "name": "Isa",
        "class": "VII",
        "subjects": ["english, math, biology"],
    },
    "id4": {
        "name": "Sam",
        "class": "VII",
        "subjects": ["english, math, biology"],
    }
}
result = {}

for key,value in student.items():
    if value not in result.values():
        result[key] = value
        #This is how you add something to a dictionary

print(result)
