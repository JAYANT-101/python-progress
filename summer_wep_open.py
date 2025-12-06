import Swimmer_data
import os
import webbrowser

PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
DIR = r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"
data = Swimmer_data.file_opener(PATH, DIR)

for name in data["Calvin"]:
    webbrowser.open("file://"+r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"+name)