with open("file.txt", "w") as file:  # "w" mode allows writing (overwrites file)
    file.write("new text")  # No need to store the return value

with open("file.txt", "a") as file:
    file.write("\nnew text 2") 
    
with open("file.txt", "r") as file:  # Open again in read mode to read contents
    contents = file.read()
    print(contents)  # This will print "new text"

