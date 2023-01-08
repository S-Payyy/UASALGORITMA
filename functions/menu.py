from rich.table import Table
from rich.console import Console
import os
from datetime import datetime
class FUNCTION:
    def __init__(self) -> None:
        pass

    def create_empty_table(self,*args):
        tab = Table()
        for i in args:
            tab.add_column(i)
        for i in args:
            tab.add_row("")
        return tab

    def tabClear():
        osname = os.name
        match osname:
            case "posix": os.system('clear')
            case "nt": os.system("cls")

class MENU(FUNCTION):
    def __init__(self,db) -> None:
        self.db = db
        conn = create_connection(db)
        self.cur = conn.cursor()
        self.conn = conn

    def BMasuk(self):
        cur = self.cur
        conn = self.conn
        tab = Table()
        cons = Console()
        cur.execute("SELECT * FROM logMasuk")
        data = cur.fetchall()
        col = ["ID","Name","Jumlah","Date"]
        for c in col:
            tab.add_column(c)
        for i in data:
            #print(f"{i[0]}, Barang {i[1]} masuk sebanyak {i[2]} pada {i[3]}")
            tab.add_row(f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}")
        cons.print(tab)
        
    def BKeluar(self):
        cur = self.cur
        conn = self.conn
        tab = Table()
        cons = Console()
        cur.execute("SELECT * FROM logKeluar")
        data = cur.fetchall()
        col = ["ID","Name","Jumlah","Date"]
        for c in col:
            tab.add_column(c)
        for i in data:
            #print(f"{i[0]}, Barang {i[1]} keluar sebanyak {i[2]} pada {i[3]}")
            tab.add_row(f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}")
        cons.print(tab)

    def DBarang(self):
        cur = self.cur
        cur.execute("SELECT * FROM product")
        rows = cur.fetchall()
        col = ["No","Code Barang","Nama","Berat","Harga","Jumlah"]
        n = 0
        tab = Table()
        cons = Console()
        for a in col:
            tab.add_column(a)
        for i in rows:
            # row 0 = code
            # row 1 = nama
            # row 2 = berat
            # row 3 = harga
            # row 4 = jumlah barang
            n+=1
            tab.add_row(f"{n}",f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}",f"{i[4]}")
        cons.print(tab)

    def CBarang(self,ids):
        try:
            ids = int(ids)
        except:
            if type(ids) != int :ids = 1
            else:pass
        tab = Table()
        cons = Console()
        cur = self.cur
        col = ["No","Code Barang","Nama","Berat","Harga","Jumlah"]
        cur.execute("SELECT * FROM product WHERE id={}".format(ids))
        try:
            i = cur.fetchone()
            for x in col:
                tab.add_column(x)
            tab.add_row("1",f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}",f"{i[4]}")
            cons.print(tab)
        except:
            FUNCTION.create_empty_table(col)
            cons.print(tab)

    def THBarang(self):
        cur = self.cur
        def logs1(name,jumlah):
                date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                cur.execute(f"INSERT INTO logMasuk (name,jumlah,date)VALUES ('{name}','{jumlah}','{date}')")
                self.conn.commit()
        def logs2(name,jumlah):
                date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                cur.execute(f"INSERT INTO logKeluar (name,jumlah,date)VALUES ('{name}','{jumlah}','{date}')")
                self.conn.commit()
        def Tambah():
            ids = input("Masukan ID Barang : ")
            try:
                cur.execute(f"SELECT name,jumlah FROM product WHERE id = '{ids}'")
                datas = cur.fetchall()
                i = datas[0]
                print(f"Stock Barang {i[0]} : {i[1]}\n")
                add = input("Jumlah barang masuk : ")
                total = i[1] + int(add)
                cur.execute(f"UPDATE product SET jumlah = {total} WHERE id = '{ids}'")
                self.conn.commit()
                logs1(i[0],add)
                FUNCTION.tabClear()
                print(f"Stock barang {i[0]} tersisa {total}")
            except:
                name = input("Masukan Nama Produk : ")
                berat = input("Masukan Berat Produk : ")
                harga = input("Masukan Harga Produk : ")
                jumlah = input("Masukan Jumlah Produk : ")
                cur.execute(f"INSERT INTO product VALUES ('{ids}','{name}','{berat}','{harga}','{jumlah}')")
                self.conn.commit()
                logs1(name,jumlah)
                FUNCTION.tabClear()
                print(f"{name} berhasil ditambahkan sebanyak {jumlah}.")
        def Kurang():
            ids = input("Masukan ID Barang : ")
            try:
                cur.execute(f"SELECT name,jumlah FROM product WHERE id = '{ids}'")
                datas = cur.fetchall()
                i = datas[0]
                print(f"Stock Barang {i[0]} : {i[1]}\n")
                re = int(input("Jumlah barang keluar : "))
                if i[1] - re <= 0:
                    FUNCTION.tabClear()
                    print("Stok barang tidak cukup.")
                else:
                    total = i[1] - re
                    cur.execute(f"UPDATE product SET jumlah = {total} WHERE id = '{ids}'")
                    self.conn.commit()
                    logs2(i[0],re)
                    FUNCTION.tabClear()
                    print(f"Stock barang {i[0]} tersisa {total}")
            except:
                print("Code Barang tidak tersedia.")
                FUNCTION.tabClear()
        while True:
            print("\t\tWarehouse Management")
            print(52*"="+"\n1. Masukan Barang\n2. Keluarkan Barang\n3. Kembali\n"+52*"=")
            THmenu = input("mode > ")
            match THmenu:
                case "1":Tambah()
                case "2":Kurang()
                case "3":break
                case _:print("Pilihan Salah!")

def create_connection(db_file):
    import sqlite3
    """ create a database connection to the SQLite database
        specified by db_file
    db_file database file
    return Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print("Database Failed!")
    return conn

def Main(db):
    while True:
        FUNCTION.tabClear()
        menu = ["Data Barang Masuk","Data Barang Keluar","Data Gudang","Cek Barang","Tambah/Hapus Barang"]
        print("\n\n\t\tMenu Inventory Gudang")
        print(52*"=")
        n = 0
        for i in menu:
            n+=1
            print(f"{n}. {i}")
        print(52*"=")
        ch = input("Menu > ")
        match ch:
            case "1" : MENU(db).BMasuk()
            case "2" : MENU(db).BKeluar()
            case "3" : MENU(db).DBarang()
            case "4" : MENU(db).CBarang(input("Masukan Code Barang : "))
            case "5" : MENU(db).THBarang()
            case _ : print("Pilihan Salah!")
        rerun = input("Kembali ? y/n ")
        if rerun in ["y","yes","ya"]:
            continue
        else:
            break
# Testing Code
