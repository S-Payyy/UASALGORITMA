import os

from functions import menu
### Peringatan Jangan di Maling Codenya :) nanti eror nangges.
### Peringatan Jangan di Maling Codenya :) nanti eror nangges.
### Peringatan Jangan di Maling Codenya :) nanti eror nangges.
### Peringatan Jangan di Maling Codenya :) nanti eror nangges.
### Peringatan Jangan di Maling Codenya :) nanti eror nangges.

def tabClear():
    osname = os.name
    match osname:
        case "posix": os.system('clear')
        case "nt": os.system("cls")

def main(db):
    while True:
        tabClear()
        print("""
        Kelompok BIBD
        Tema : Program Inventory Gudang
        Anggota:
            1. Muhamad Rifai (2270231011)
            2. Denis Lie Farel (2270231024)
            3. Muhammad Reza Alifa (2270231004) 
            4. Dafa Haikal Kamil Nasution (2270231010)
            5. Rafi Pratama (2270231036)
        """)
        print(52*"=")
        run = input("Mulai Program ? y/n ").lower()
        if run in ["y","yes","ya"]:
            tabClear()
            menu.Main(db)
        else:
            print("Exiting Programs. . .")
            break

if __name__ == "__main__":
    db = input("Input Database Path : ")
    main(db)