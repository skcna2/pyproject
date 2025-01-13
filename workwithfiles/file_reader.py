from pathlib import Path

path = Path('workwithfiles/pi_digits.txt')
contents = path.read_text()
content_lines = contents.splitlines()
pi_string = ''
a = 1

for line in content_lines:
    pi_string += line.rstrip() 
    

print(pi_string)
print(len(pi_string))
    

