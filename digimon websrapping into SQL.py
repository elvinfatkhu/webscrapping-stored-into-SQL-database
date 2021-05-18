import json
import requests
from bs4 import BeautifulSoup
import mysql.connector


#TUGAS digidbPySQL Elvin Fatkhunnuha

myDB = {
    "user": "root",
    "password": "elvin21",
    "host" : "localhost",
    "database": "digimon"

}
conn = mysql.connector.connect(**myDB)

Cr = conn.cursor()


"""

query = "CREATE TABLE digidb(No SmallInt(25), Nama char(25), ImageLink varchar(300), Stage char(25), Type char(25), Attribute char(25), Memory SmallInt(25), EquipSlots SmallInt(25), HP SmallInt(25), SP SmallInt(25), Atk SmallInt(25), Def SmallInt(25), Intel SmallInt(25) Spd SmallInt(25)) "
Cr.execute(query)
print('Success')

"""

url = 'http://digidb.io/digimon-list/'
web = requests.get(url)
out = BeautifulSoup(web.content,'html.parser')
data = out.find_all('tr', class_='')

for i in range(len(data)):
    obj = data[i]
    stats = obj.find_all('center') #<center>
    no = int(obj.b.text) # </b>
    nama = obj.a.text #</a>
    image = obj.img['src']  
    stage = stats[0].text
    types = stats[1].text
    attribute = stats[2].text
    memory = int(stats[3].text)
    equip = int(stats[4].text)
    hp = int(stats[5].text)
    sp = int(stats[6].text)
    atk = int(stats[7].text)
    defence = int(stats[8].text)
    intel = int(stats[9].text)
    spd = int(stats[10].text)

    sql = "INSERT INTO digidb VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (no, nama, image, stage, types, attribute, memory, equip, hp, sp, atk, defence,intel,spd)
    Cr.execute(sql,val)
    conn.commit()
    print("Data submitted")
