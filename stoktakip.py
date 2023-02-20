from tkinter import *
from tkinter import messagebox
from pathlib import Path
import sqlite3 as sql
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def sorgula(barkod):
    db=sql.connect("urunler.db")
    cursor = db.cursor() 
    cursor.execute(f"SELECT * FROM 'urunler' WHERE barkod={barkod}  ")

    urun = cursor.fetchall()
    
    sonuc=len(urun)
    
    if(sonuc!=0):
        text=f"{urun[0][2]} fiyat={urun[0][3]} TL {urun[0][4]} Adet mevcut"
        messagebox.showwarning("Bulundu",text)
        
        
    else:

        
        messagebox.showwarning("Hata!", "Böyle bir ürün yok")
try:


    def basildi():
        barkod=entry_1.get()
        sorgula(barkod)

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\emira\Desktop\build\assets\frame0")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window = Tk()

    window.geometry("959x500")
    window.configure(bg = "#FFFFFF")
    window.title("Stok Takip")
    window.iconbitmap('packages.ico')
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 500,
        width = 959,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        651.5,
        100.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=409.0,
        y=63.0,
        width=485.0,
        height=72.0
    )

    canvas.create_text(
        207.0,
        80.0,
        anchor="nw",
        text="BARKOD",
        fill="#000000",
        font=("Inter Bold", 36 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: basildi(),
        relief="flat"
    )
    button_1.place(
        x=61.0,
        y=194.0,
        width=884.0,
        height=89.0
    )

    window.resizable(False, False)
    window.mainloop()

except :
    messagebox.showwarning("Hata!", "Program da bir hata var lütfen yazılımcıyla iletişime geçiniz!")


"""
1)git clone https://github.com/ParthJadhav/Tkinter-Designer.git

2)Designeri açmak için
    cd Tkinter-Designer
    cd gui
    python gui.py

3)Figmada Tasarm 
    tasrım urls
    hesap tokenı
"""


