# Laporan Praktikum Kriptografi
Minggu ke-: 13
Topik: TinyChain – Proof of Work
Nama: Asadila Haila Hamada 
NIM: 230202801  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
Tiny Chain adalah blockchain sederhana yang digunakan untuk mempelajari konsep dasar blockcahin, termasuk mekanisme konsesnsus Proof of Work. Dalam TinyChain, POW mengharuskan node mencari nilai nonce yang menghasilkan hash sesuai kriteria tertentu sebelum sebuah blok dapat ditambahkan, sehingga proses validasi berlangsung secara terdesentralisasi

Meskipun tingkat kesulitanya dibuat ringan agar dapat dijalankan pada kompiter biasa, POW pada TinyChain tetap menunjukan peranya dalam menjaga kintegritas data dan mencegah manipulasi blok. Disisi lain TinyChain juga menggambarkan keterbatasan POW, seperti kebutuhan sumber data dan masalah skalabilitas, sehingga berfungsi sebagai model belajar untuk memahami kelebihan dan kekurangan POW dalam sistem blockchain

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 — Membuat Struktur Blok
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
Langkah 2 — Membuat Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
Langkah 3 — Analisis Proof of Work
Perhatikan bahwa proses mining membutuhkan waktu (bergantung pada difficulty).
Analisis: semakin tinggi difficulty, semakin lama proses mining.
Diskusikan bagaimana hal ini menjamin keamanan blockchain.


---

## 5. Source Code
# membuat struktur block chain 
---
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")
---
# membuat block chain 
---
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Fungsi hash sangat penting karena digunakan untuk mengamankan data blok satu dengan lainya, serta memastikan bahwa perubahan data dapat langsung terdeteksi
2. POW mencegah double spending dengan mewajibkan penambang memcah teka teki kriptografi dan menyetujui satu rantai blok yang sah, sehingga satu transaksi tidak dapat dicatat lebih dari skali
3. Kelemahan POW adalah kebutuhan komputasi yang tinggi, karena banyak node melakukan perhitungan secara bersamaan, yang menyebabkan konsumsi listrik besar dan kurang efesien untuk skala besar
---

## 8. Kesimpulan
Hasil dari percobaan TinyChain, fungsi hash menjaga integritas blockchain karena perubahan kecil langsung membuat rantai tidak valid. POW memaksa proses komputasi sebelum menambah blok sehingga mencegah double speending, namun semakin tinggi tingkat kesulitan, proses mining menjadi lebih lambat dan boros sumber daya

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
