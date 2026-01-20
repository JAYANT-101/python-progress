from flask import Flask, session, render_template, request
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

@app.get("/swimmer")
def summer():
    populate_session()
    return str(sorted(session["data"]))

@app.get("/files/<summers>")
def get_summer_data(summers):
    populate_session()
    return str(session["data"][summers])

@app.get("/swimmers")
def display_swimmer():
    populate_session()
    return render_template("select.html",
                           title="Select swimmer",
                           url="/showfile",
                           select_id="swimmer",
                           data=sorted(session["data"]))

@app.post("/showfiles")
def display_swimmers_files():
    populate_session()
    name = request.form["swimmer"]
    return render_template(
        "select.html",
        title="Select an event",
        url="/showbarchart",
        select_id="file",
        data=session["data"][name],
    )

if __name__ == "__main__":
    app.run(debug=True)