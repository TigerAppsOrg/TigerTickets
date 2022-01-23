DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS TRANSACTIONS;
DROP TABLE IF EXISTS TICKETS;
DROP TABLE IF EXISTS CANCELEDTRANSACTIONS;
DROP TABLE IF EXISTS NOTIFY;
DROP TABLE IF EXISTS report;
CREATE TABLE users (
     netid VARCHAR NOT NULL,
     PRIMARY KEY (netid)
);
CREATE TABLE transactions (
     transactionid SERIAL UNIQUE,
     sellerid VARCHAR NOT NULL,
     buyerid VARCHAR NOT NULL,
     ticketid SERIAL UNIQUE,
     status VARCHAR NOT NULL,
     time timestamp without time zone,
     PRIMARY KEY (transactionid)
);
CREATE TABLE tickets (
     ticketid SERIAL UNIQUE,
     time timestamp without time zone,
     event VARCHAR NOT NULL,
     sellerid VARCHAR NOT NULL,
     price INT,
     type VARCHAR NOT NULL,
     description VARCHAR,
     status VARCHAR NOT NULL,
     other VARCHAR NOT NULL,
     timeadded timestamp without time zone,
     fullname VARCHAR NOT NULL,
     PRIMARY KEY (ticketid)
);

CREATE TABLE canceledtransactions (
     transactionid INT UNIQUE,
     sellerid VARCHAR NOT NULL,
     buyerid VARCHAR NOT NULL,
     ticketid INT,
     status VARCHAR NOT NULL,
     time timestamp without time zone,
     PRIMARY KEY (transactionid)
);

CREATE TABLE notify (
     notificationid SERIAL UNIQUE,
     time timestamp without time zone,
     event VARCHAR NOT NULL,
     buyerid VARCHAR NOT NULL,
     price INT,
     type VARCHAR NOT NULL,
     status VARCHAR NOT NULL,
     other VARCHAR NOT NULL,
     timeadded timestamp without time zone,
     PRIMARY KEY (notificationid)
);

CREATE TABLE report (
     repid SERIAL UNIQUE,
     reportid VARCHAR,
     report VARCHAR,
     bug VARCHAR,
     PRIMARY KEY (repid)
);
