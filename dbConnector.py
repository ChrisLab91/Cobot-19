#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='root', database='blogDB')
cursor = mariadb_connection.cursor()

first_name="Maggy"
last_name="Anonymous"

print("wow")
content={'name': 'michael', 'address': {'address': 'lindwurmstraße 115', 'town': 'münchen', 'name': 'holland'}, 'info': '', 'type': 'Gassi Gehen'}
cursor.execute("INSERT INTO user (first_name,last_name, id,username, adress_user_id) VALUES (%s,%s,LAST_INSERT_ID()+100,%s,LAST_INSERT_ID()+101)", (content["name"], content["name"],content["name"]))
cursor.execute("INSERT INTO adress (id, addition, city, country, house_number,street) VALUES (LAST_INSERT_ID()+101,'a',%s,%s,%s,%s)", (content["address"]["town"],"germany", 0,content["address"]["address"]))
cursor.execute("INSERT INTO task (text,title,request_user_id, help_user_id, id) VALUES (%s,%s,LAST_INSERT_ID()+100, NULL, LAST_INSERT_ID()+102)", (content["info"],content["type"]))
mariadb_connection.commit()


