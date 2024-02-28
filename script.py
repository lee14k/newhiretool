file_path='data.txt'
with open (file_path, 'r') as file:
    lines = file.readlines()

modified_lines=[]
for line in lines:
    if "DOB: " in line:
        line=line.replace('/', '')
    modified_lines.append(line)
with open (file_path, 'w') as file:
    file.writelines(modified_lines)