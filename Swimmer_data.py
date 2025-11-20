import os
import pandas as pd
import statistics

tdata={}

def open_and_convert(filename, root_name):
    label = file_name[:-4].split('-')
    file_path = os.path.join(root_name, filename)  # Construct the full file path
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            replacements = content.maketrans(":.", "  ")
            new_content = content.translate(replacements)
            data = new_content.strip().split(',')
            convert_time = []
            for i in range(len(data)):
                time = data[i].split(' ')
                if len(time) >= 3:
                    mint, sec, milsec = time
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))
                else:
                    convert_time.append((int(sec) * 100) + int(milsec))

            cpu = tuple(label)
            raw_avg_time = statistics.mean(convert_time)
            tdata[cpu] = data, raw_avg_time
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

PATH =r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
for root, dirs, files in os.walk(PATH):
    for file_name in files:
        data=open_and_convert(file_name, root)

print(tdata)