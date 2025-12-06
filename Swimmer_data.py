import os
import statistics
import Scaler
import time

start_time = time.time()

def make_html(details, times, avg_time, raw_time, file_location):
    """this make html"""

    name, age, distance, stroke = details
    top = f"""<!DOCTYPE html>
<html>
    <head>
        <title>
            {name}-{age}-{distance}-{stroke}
        </title>
    </head>
    <body>
        <h3>{name}-{age}-{distance}-{stroke}</h3>"""
    middle = ""
    for i in range(len(times)-1, -1, -1):
        bar_wreath = Scaler.scaled_number(raw_time[i], 0, max(raw_time), 0, 350)
        middle = middle + f"""
        <svg height="30" width="400">
            <rect height="30" width="{bar_wreath}" style="fill:rgb(0,0,255);" />
        </svg>{times[i]}<br />"""
    lower = f"""<p>Average:{avg_time}</p>
    </body>
</html>"""
    try:
        # os.makedirs(file_location)
        with open(f"{file_location}/{name}-{age}-{distance}-{stroke}.html", "w") as file:
            file.write(top+middle+lower)
    except Exception as e:
        return f"Error reading {file_location}: {e}"

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
                    mint, sec, milsec = times
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))
                else:
                    mint = 0
                    sec, milsec = times
                    convert_time.append((int(mint) * 60 * 100) + (int(sec) * 100) + int(milsec))

            raw_avg_time = statistics.mean(convert_time)
            min_sec, milsec = f"{raw_avg_time / 100:.2f}".split('.')
            mint = int(min_sec) // 60
            sec = int(min_sec) - mint * 60
            string_time = f"{mint}:{sec:0>2}.{milsec}"
            return label, filedata, string_time, convert_time

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def file_opener(path, DIR):
    """This function will call the open_and_convert() function this module in a for-loop to get the data to make a chart
     this function takes one argument which is path the path is the location of the folder the swimmer's data is in and
     the out path to store the html file and also calls make_html() this return list of names ok"""

    for root, dirs, files in os.walk(path):
        name_dic = {}
        for file_name in files:
            data = open_and_convert(file_name, root)
            summers_details, times, avg_time, convert_time = data
            name = summers_details[0]
            if name not in name_dic:
                name_dic[name] = [f"{summers_details[0]}-{summers_details[1]}-{summers_details[2]}-{summers_details[3]}.txt"]
            else:
                name_dic[name].append(f"{summers_details[0]}-{summers_details[1]}-{summers_details[2]}-{summers_details[3]}.txt")
            make_html(summers_details, times, avg_time, convert_time, DIR)
        return name_dic
    return None

PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
DIR = r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"

print(file_opener(PATH, DIR))
end_time = time.time()
print(end_time - start_time)
