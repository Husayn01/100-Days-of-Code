# Creating a Python dictionary
my_dictionary = {
    "name": "Hussaini Ahmed",
    "age": 18,
    "occupation": "Student",
    "university": "Federal University of Technology, Minna",
    "interests": ["Geology", "Data Analysis", "GIS"],
    "skills": {
        "programming_languages": ["Python", "SQL"],
        "tools": ["ArcGIS", "QGIS", "Rockworks"]
    },
}
my_dictionary["location"] = "Minna, Nigeria"

print(my_dictionary["location"])
print(my_dictionary["skills"]["tools"][1])

for key in my_dictionary:
    print(key)
    print(my_dictionary[key])

for i in my_dictionary['interests']:
    print(i)

lists = ["a", "b", ["c", "d"]]
print(lists[2][0])