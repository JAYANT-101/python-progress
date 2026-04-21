import DBcm

db_details = "CoachDB.sqlite3"

import os

FOLDER = "swimdata/"

files = os.listdir(FOLDER)
# files.remove(".DS_Store"


SQL_SELECT_SWIMMERS = """
    select * from swimmers
    where name = %s and age = %s
"""

SQL_INSERT_SWIMMERS = """
    insert into swimmers
    (name, age)
    values
    (%s, %s)
"""

SQL_SELECT_EVENTS = """
    select * from events
    where distance = %s and stroke = %s
"""

SQL_INSERT_EVENTS = """
    insert into events
    (distance, stroke)
    values
    (%s, %s)
"""

SQL_GET_SWIMMER = """
    select id from swimmers
    where name = %s and age = %s
"""

SQL_GET_EVENT = """
    select id from events
    where distance = %s and stroke = %s
"""

SQL_INSERT_TIMES = """
    insert into times
    (swimmer_id, event_id, time)
    values
    (%s, %s, %s)
"""


with DBcm.UseDatabase(db_details) as db:
    for fn in files:
        name, age, distance, stroke = fn.removesuffix(".txt").split("-")

        db.execute(
            SQL_SELECT_SWIMMERS,
            (
                name,
                age,
            ),
        )
        if not db.fetchall():
            db.execute(
                SQL_INSERT_SWIMMERS,
                (
                    name,
                    age,
                ),
            )

        db.execute(
            SQL_SELECT_EVENTS,
            (
                distance,
                stroke,
            ),
        )
        if not db.fetchall():
            db.execute(
                SQL_INSERT_EVENTS,
                (
                    distance,
                    stroke,
                ),
            )

        db.execute(
            SQL_GET_SWIMMER,
            (
                name,
                age,
            ),
        )
        s_id = db.fetchone()[0]

        db.execute(
            SQL_GET_EVENT,
            (
                distance,
                stroke,
            ),
        )
        e_id = db.fetchone()[0]

        with open(FOLDER + fn) as sf:
            times = sf.read().strip().split(",")
            for t in times:
                db.execute(
                    SQL_INSERT_TIMES,
                    (
                        s_id,
                        e_id,
                        t,
                    ),
                )