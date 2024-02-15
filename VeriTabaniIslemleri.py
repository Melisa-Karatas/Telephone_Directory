import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem

class VeriTabaniIslemleri:
    def __init__(self):
        self.connection = sqlite3.connect("Telefon_Rehberi.db")
        self.cursor = self.connection.cursor()
        
        self.cursor.execute('''
        create table if not exists rehber(
            id integer primary key autoincrement,
            ad varchar(100) not null,
            soyad varchar(150) not null,
            telefon varchar(15)
            )
                            ''')
        self.connection.commit()
        
    def VeriEkle(self, ad, soyad, telefon):
        self.cursor.execute('insert into rehber(ad, soyad, telefon) values(?,?,?)', (ad,soyad,telefon))
        self.connection.commit()
        
    def VerileriGetir(self):
        self.cursor.execute('select * from rehber')
        return self.cursor.fetchall()
    
    def VeriSil(self, row_id):
        self.cursor.execute('delete from rehber where id = ?',(row_id,))
        self.connection.commit()
        
    def VeriGuncelleme(self, row_id, ad, soyad, telefon):
        self.cursor.execute('update rehber set ad=?, soyad=?, telefon=? where id=?',(ad, soyad, telefon, row_id))
        self.connection.commit()
        
    def VerileriGetirArayuz(self, table_widget):
        table_widget.clearContents()
        data = self.VerileriGetir()
        
        table_widget.setRowCount(len(data))
        for i, row in enumerate(data):
            for j , value in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(str(value)))
                
                
        