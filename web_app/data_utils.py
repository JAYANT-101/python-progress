import DBcm
from queries import *
from web_app import queries

#DONT CHANGE
db_details = "CoachDB.sqlite3"

def session() -> int :
    """This function does not take git any arguments and returns the distinct sessions"""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SESSIONS)
        return db.fetchall()

def swimmer_by_session(date: str) -> list[tuple[str, int]]:
    """This function takes a single argument the date and returns a list of tuples
    containing name and age of the swimmers"""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_BY_SESSION, (date,))
        return db.fetchall()
def swimmer_event_by_session(name: str, age: int, date: str)-> list[tuple[str, str]]:
    """This function takes three arguments the name, age and the date and returns a list
    of tuples containing distance and the stroke"""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age, date))
        return db.fetchall()
def chart_data_by_swimmer_event_session(name: str, age:int, distance:str, stroke:str, date:str)->list[tuple[str,]]:
    """This function takes five arguments name, age, distance, stroke and date and returns
    a list of tuples containing times of the envent"""
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION, (name, age, distance, stroke, date,))
        return db.fetchall()