from flask import Flask, session, render_template
import Swimmer_data
app = Flask(__name__)
app.secret_key = "you will never guess"

@app.get("/")
def index():
    return render_template('index.html',
                           title="Welcome to the Swimclub system",)

def populate_session():
    if "data" not in session:
        PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
        DIR = r"C:\Users\jayan\PycharmProjects\python-progress\swimdatahtml"
        session["data"] = Swimmer_data.file_opener(PATH, DIR)

@app.get("/swimmers")
def summer():
    populate_session()
    return str(sorted(session["data"]))

@app.get("/files/<summers>")
def get_summer_data(summers):
    populate_session()
    return str(session["data"][summers])

if __name__ == "__main__":
    app.run(debug=True)