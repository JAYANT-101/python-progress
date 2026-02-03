from flask import Flask, session, render_template, request
import Swimmer_data
app = Flask(__name__)
app.secret_key = "you will never guess"

#fornt page
@app.get("/")
def index():
    return render_template('index.html',
                           title="Welcome to the Swimclub system",)

#This populates all function with necessary data
def populate_session():
    if "data" not in session:
        PATH = r"C:\Users\jayan\PycharmProjects\python-progress\swimdata"
        DIR = r"C:\Users\jayan\PycharmProjects\python-progress\web_app\templates"
        session["data"] = Swimmer_data.file_opener(PATH, DIR)

#This is just a test it. Shows names of all summers
@app.get("/swimmer")
def summer():
    populate_session()
    return str(sorted(session["data"]))

#This function gives summer data
@app.get("/files/<summers>")
def get_summer_data(summers):
    populate_session()
    return str(session["data"][summers])

#This creates a dropdown menu of names of the summers
@app.get("/swimmers")
def display_swimmers():
    populate_session()
    return render_template(
        "select.html",
        title="Select a swimmer",
        url="/showfiles",
        select_id="swimmer",
        data=sorted(session["data"]),
    )

#This gives a selection menu for selecting file based on names
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
#This function show the bar-charts
@app.post("/showbarchart")
def show_bar_chart():
    file_id = request.form["file"]
    return render_template(file_id)

#This just star the app
if __name__ == "__main__":
    app.run(debug=True)