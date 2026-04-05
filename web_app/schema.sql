CREATE TABLE swimmers (
        id integer not null primary key autoincrement,
        name varchar(32) not null,
        age integer not null
    );
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE events (
            id integer not null primary key autoincrement,
            distance varchar(16) not null,
            stroke varchar(16) not null
        );
CREATE TABLE times (
            swimmer_id integer not null,
            event_id integer not null,
            time varchar(16) not null,
            ts timestamp default current_timestamp
        );
