import os
import pandas as pd
import statistics

def time_convert_to_string(raw_time, category):

    if category == "50m":
        string_time = str(round(raw_time/100, 2))
        return string_time
    else:
        min_sec, milsec = str(round(raw_time/100, 2)).split('.')
        mint = int(min_sec)//60
        sec = int(min_sec) -  mint*60
        string_time = f"{mint}:{sec}.{milsec}"
        return string_time

def open_and_convert(filename, root_name):
    label = file_name[:-4].split('-')
    file_path = os.path.join(root_name, filename)  # Construct the full file path

    try:

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            filedata = content.strip().split(',')
            replacements = content.maketrans(":.", "  ")
            new_content = content.translate(replacements)
            mod_filedata = new_content.strip().split(',')

            convert_time = []
            for i in range(len(mod_filedata)):
                time = mod_filedata[i].split(' ')
                if len(time) >= 3:
                    mint, sec, milsec = time
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))
                else:
                    sec, milsec = time
                    convert_time.append((int(sec) * 100) + int(milsec))

            swimmer_details = tuple(label)
            raw_avg_time = statistics.mean(convert_time)
            total_time = time_convert_to_string(raw_avg_time, swimmer_details[2])
            return filedata, total_time, swimmer_details

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

tdata={}

PATH =r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"

for root, dirs, files in os.walk(PATH):
    for file_name in files:
        data = open_and_convert(file_name, root)
        list_of_time, raw_ang_time, swimmers_details = data
        tdata[swimmers_details] = list_of_time,raw_ang_time

print(tdata)