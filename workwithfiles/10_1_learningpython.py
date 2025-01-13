from pathlib import Path

file = Path('workwithfiles/learning_python.txt')
read_file = file.read_text()

print(read_file)

lines = read_file.splitlines()

for line in lines:
    print(f"This is the line >> {line.replace('python','PHYTON')}")


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I love working with data.\n"

read_new_file= file.write_text(contents)
print(read_file)
