try:
    file = open("./data.txt")  # Might raise FileNotFoundError
except FileNotFoundError:
    with open("./Day 30/data.py", "w") as file:
        file.write("text")
else:
    print(file.read())
finally:
    file.close()
    print("File is closed")

# Separate try block for KeyError
try:
    obj = {"key": "value"}
    print(obj["another_key"])  # This will now raise KeyError
except KeyError as err_msg:
    print(f"That key {err_msg} does not exist")
