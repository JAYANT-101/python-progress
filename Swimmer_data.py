import os
import pandas as pd
import statistics
import time

start_time = time.time()

def open_and_convert(filename, root_name):
    """this function will take to arguments file name and the root the files are in then it will open thous file read the data
     and then calculate the avg time and convert that avg time to sting. this function returns three variables label which have
     the swimmer's data, filedata the data in the file and string time which is the avg time of the swimmer's in string"""
    label = filename[:-4].split('-')
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
                times = mod_filedata[i].split(' ')
                if len(times) >= 3:
                    mint, sec, milsec = time
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))
                else:
                    mint = 0
                    sec, milsec = time
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))

            raw_avg_time = statistics.mean(convert_time)
            min_sec, milsec = str(round(raw_avg_time / 100, 2)).split('.')
            mint = int(min_sec) // 60
            sec = int(min_sec) - mint * 60
            string_time = f"{mint}:{sec}.{milsec}"
            return label, filedata, string_time, convert_time

    except Exception as e:
        print(f"Error reading {file_path}: {e}")


def file_opener(path):
    """This function will call the open_and_convert() function this module in a for-loop to get the data to make a chart
     this function takes one argument which is path the path is the location of the folder the swimmer's data is in """
    full_data = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            data = open_and_convert(file_name, root)
            full_data.append(data)
        return full_data
    return None


PATH =r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"


print(file_opener(PATH))
end_time = time.time()
print(end_time - start_time)
