import sqlite3
import smtplib
from random import *
from urllib.parse import urlparse
from urllib.parse import parse_qs
import socket

def get_time(event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        select_time = "select Date_Time from Events where event_ID = ?"
        cursor.execute(select_time, (event_ID, ))
        time = cursor.fetchone()[0]
        return(time)

def update_status(event_ID, status):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        set_status = "update Events Set Status = ? where event_ID = ?"
        cursor.execute(set_status, (status, event_ID))
        user_ID = cursor.fetchall()

def get_contacts(user_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        select_contact = "select contact_1 from Users where user_ID = ?"
        cursor.execute(select_contact, (user_ID, ))
        c1 = cursor.fetchone()[0]
        select_contact = "select contact_2 from Users where user_ID = ?"
        cursor.execute(select_contact, (user_ID, ))
        c2 = cursor.fetchone()[0]
        select_contact = "select contact_3 from Users where user_ID = ?"
        cursor.execute(select_contact, (user_ID, ))
        c3 = cursor.fetchone()[0]
        current_contacts = [c1, c2, c3]
        return(current_contacts)


def get_name(event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        select_user_ID = "select User from Events where event_ID = ?"
        cursor.execute(select_user_ID, (event_ID, ))
        user_ID = cursor.fetchall()
        for x in user_ID:
             ID = x
        for x in ID:
            user_ID = x
        select_username = "select Name from Users where user_ID = ?"
        cursor.execute(select_username, (user_ID, ))
        name = cursor.fetchall()
        for x in name:
            n = x
        for x in n:
            name = x
        return(name)

def get_longitude(event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        select_long = "select Longitude from Events where event_ID = ?"
        cursor.execute(select_long, (event_ID, ))
        long= cursor.fetchone()[0]
        return(long)

def get_latitude(event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        select_lat = "select Latitude from Events where event_ID = ?"
        cursor.execute(select_lat, (event_ID, ))
        lat= cursor.fetchone()[0]
        return(lat)


def parse_url(url, parameter):
    qs = urlparse(url, allow_fragments=True).query
    paramlis = parse_qs(qs)[parameter]
    for x in paramlis:
        returnvalue = x
    return(returnvalue)

def generate_code(event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        IP = socket.gethostbyname(socket.gethostname())
        link = "http://"+IP+"/drw_server/map.cgi?token=" + str(event_ID)
        return(link)

def send_email(recipient, link):
    if recipient=='' or recipient== 'NULL':
        return()
    sender = 'HotLegume2018@gmail.com'
    receiver  = recipient
    body = 'Someone you know has activated a safety app on their phone. Click the link to access more information: ' + link
    subject = 'Someone you know May be in Danger'
    username = 'HotLegume2018@gmail.com'
    password = 'l3gume!!!'
    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(recipient), subject, body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, receiver, message)
    server.quit()

def contact(user_ID, event_ID):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        link = generate_code(event_ID)
        select_contacts = "select contact_1, contact_2, contact_3 from Users where user_ID = ?"
        cursor.execute(select_contacts, (user_ID, ))
        contacts = cursor.fetchall()
        for contact in contacts:
            send_email(contact, link)


def add_event(user_ID, time, longitude, latitude, status):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        num_IDs = []
        cursor.execute("select event_ID from Events")
        existing_IDs = cursor.fetchall()
        for id in existing_IDs:
            num_IDs.append(id[0])
        ID = randint(100000, 999999)
        while(True):
            if ID in num_IDs:
                ID = randint(10000, 99999)
                continue
            else:
                break
        new_event = "insert into Events (event_ID, User, Date_Time, Longitude, Latitude, Status) values(?,?,?,?,?,?)"
        values = (ID, user_ID, time, longitude, latitude, status)
        cursor.execute(new_event, values)
        db.commit()
        return(ID)




def add_contacts(user_ID, contact_1, contact_2, contact_3):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        contacts = "update Users Set contact_1 = ?, contact_2 = ?, contact_3 = ? where user_ID = ?"
        values = (contact_1, contact_2, contact_3, user_ID)
        cursor.execute(contacts, values)
        db.commit()

def create_user(name):
    with sqlite3.connect("DRW_info.db") as db:
        cursor = db.cursor()
        new_user = "insert into Users (user_ID, Name) values(?,?)"
        num_IDs = []
        cursor.execute("select user_ID from Users")
        existing_IDs = cursor.fetchall()
        for id in existing_IDs:
            num_IDs.append(id[0])
        ID = randint(10000, 99999)
        while(True):
            if ID in num_IDs:
                ID = randint(10000, 99999)
                continue
            else:
                values = (ID, name)
                break
        cursor.execute(new_user, values)
        db.commit()
        return(ID)



def setup_database(db_name, users, events):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute(users)
        db.commit()
        cursor = db.cursor()
        cursor.execute(events)
        db.commit()
