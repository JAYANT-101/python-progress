import os
import pandas as pd
tdata={}
PATH =r"C:\Users\jayan\PycharmProjects\python-progress/swimdata"
for root, dirs, files in os.walk(PATH):
    for file_name in files:
        label=file_name[:-4].split('-')
        file_path = os.path.join(root, file_name)  # Construct the full file path
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                replacements = content.maketrans(":.","  ")
                new_content = content.translate(replacements)
                data = new_content.strip().split(',')
                cpu=tuple(label)
                tdata[cpu] = data
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
print(tdata)