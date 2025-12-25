from flask import Flask, sessions
import Swimmer_data
app = Flask(__name__)

# @app.get("/")
# def index():
#     return "This a place holder for the web app's opening page"

@app.get("/swimmers")
def summer():
    PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
    DIR = r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"
    data = Swimmer_data.file_opener(PATH, DIR)
    return str(sorted(data))
@app.get("/files/<summer>")
def get_summer_data(summer):
    return str(data(summer))


if __name__ == "__main__":
    app.run(debug=True)
    app.secret_key="you will never guess"
