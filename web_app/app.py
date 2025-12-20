from flask import Flask
import Swimmer_data
app = Flask(__name__)

# @app.get("/")
# def index():
#     return "This a place holder for the web app's opening page"

@app.get("/")
def summer():
    PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
    DIR = r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"
    data = Swimmer_data.file_opener(PATH, DIR)
    return str(data)


if __name__ == "__main__":
    app.run()
