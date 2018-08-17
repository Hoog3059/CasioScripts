import os

print("Format Casio Basic to be readable by calculator.")
filename = input("What file to format? : ")

output = ""
with open(filename, "r") as file:

    for i, line in enumerate(file.readlines()):
        line = line.replace("    ", "")
        if i == 0:
            output += line
            continue
        
        if not line.startswith('#') and not line.startswith('\'') and line != "\n":
            output += line

new_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "format\\", os.path.basename(filename))
with open(new_path, "w+")  as file:
    file.write(output)

print("Finished")
