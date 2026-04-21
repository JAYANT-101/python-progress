from flask import Flask, session, render_template, request
import Swimmer_data
import data_utils as du

app = Flask(__name__)
#encrepty this
app.secret_key = "1284394123ABC@!"

#fornt page
@app.get("/")
def index():
    return render_template('index.html',
                           title="Welcome to the Swimclub",)


#This display the name of the swimmer by the session
@app.post("/swimmers")
def display_swimmers():
    session["chosen_date"] = request.form["chosen_date"]
    data = du.swimmer_by_session(session["chosen_date"])
    swimmers = [f"{name}-{age}" for name, age in data]
    return render_template(
        "select.html",
        title="Select a swimmer",
        url="/showevents",
        select_id="swimmer",
        data=sorted(swimmers),
    )

#This creates a dropdown menu of sessions of the summers
@app.get("/swims")
def display_swim_sessions():
    data = du.session()
    ##dates = [sessions[0].split(" ")[0] for sessions in data]
    dates = [str(sessions[0].date()) for sessions in data]
    return render_template(
        "select.html",
        tile="Select a swim session",
        url="/swimmers",
        select_id="chosen_date",
        data=dates,
    )

#This gives a selection menu for selecting file based on names
@app.post("/showevents")
def display_swimmers_events():
    session["name"], session["age"] = request.form["swimmer"].split("-")
    data = du.swimmer_event_by_session(session["name"], session["age"], session["chosen_date"])
    events = [f"{distance} {stroke}" for distance, stroke in data]
    return render_template(
        "select.html",
        title="Select an event",
        url="/showbarchart",
        select_id="event",
        data=events,
    )
#This function show the bar-charts
@app.post("/showbarchart")
def show_bar_chart():
    distance, stroke = request.form["event"].split(" ")
    data = du.chart_data_by_swimmer_event_session(
        session["name"],
        session["age"],
        distance,
        stroke,
        session["chosen_date"],
    )
    times = [time[0] for time in data]
    average_str, times_reversed, scaled = Swimmer_data.perform_conversions(times)
    world_records = Swimmer_data.get_worlds(distance, stroke)
    header = f"{session['name']} (Under {session['age']}) {distance} {stroke} - {session['chosen_date']}"
    return render_template(
        "chart.html",
        title=header,
        data=list(zip(times_reversed, scaled)),
        average=average_str,
        worlds=world_records,
    )

#This just star the app
if __name__ == "__main__":
    app.run(debug=True)