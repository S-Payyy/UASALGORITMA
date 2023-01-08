import sqlite3
database = "C:\\Users\\OSIE\\Desktop\\UASALGO\\database.db"
conn = sqlite3.connect(database)
cur = conn.cursor()
data = (("Teh pucuk",8996001600146, 350,3000,10),("Aqua",8886008101336, 330,3000,10),("Pocari",8997035563414, 500,7000,10),("Aqua",8886008101091,1500,5000,10),("Teh Botol",8996006855145, 450,5000,10),("Yupi", 8992741983396, 15,1000,10),("Nextar", 8998175539221, 34,2000,10),("Chochopie", 8990333811126, 26,2000,10),("Big rolls", 8993175551540, 16,2000,10),("Choki choki stik",8996001313626, 24,2000,10),("Frisen flag saset coklat",18992753102006, 38,1500,10),("Sari Gandum",8996001308042, 36,2000,10),("Choki-Choki", 8996001370063, 9,2000,10),("Susu Frisian Flag vanila sachet" ,8992753031894, 38,1500,10),("Kopi ABC susu", 8991002101630, 30,1500,10),("Kopi ABC moca", 8991002101746, 30,1500,10),("Kopi Good Day capuccino",8991002103764, 25,2000,10),("Kopi Good Day Mocaccino",8991002103238, 20,1500,10),("Kopi indocafe mix",9311931024036, 20,1500,10),("Kopi Kapal api",8991002105485, 24,1500,10))
for i in data:
    ids = i[1]
    name = i[0]
    berat = i[2]
    harga = i[3]
    jumlah = i[4]
    datas = (ids,name,berat,harga,jumlah)
    cur.execute("INSERT INTO product VALUES (?,?,?,?,?);",datas)
    conn.commit()
    print(f"{i[0]}, Berhasil ditambahkan")