# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: Cryposystem (Komponen, Enkripsi & Deskripsi, Simestris & Asimetris )
Nama: Asadila Haila Hamada
NIM: 230202801
Kelas: 5 IKRA  

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2. Menggambarkan proses enkripsi dan dekripsi sederhana.
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).
---

## 2. Dasar Teori
Cryptosystem adalah sistem kriptografi yang digunakan untuk melindungi data atau pesan dengan cara mengubahnya menjadi bentuk yang tidak dapat dibaca (ciphertext) melalui proses enkripsi, dan kemudian mengembalikannya ke bentuk semula (plaintext) melalui dekripsi. Sistem ini menggunakan algoritma dan kunci rahasia yang menjadi pusat keamanannya. Tujuannya adalah menjaga kerahasiaan, keaslian, dan integritas data agar hanya pihak yang berwenang dapat mengakses informasi tersebut.

Terdapat dua jenis utama cryptosystem, yaitu symmetric key (menggunakan satu kunci yang sama untuk enkripsi dan dekripsi) dan asymmetric key (menggunakan dua kunci berbeda: publik dan privat). Cryptosystem banyak diterapkan dalam berbagai bidang seperti keamanan jaringan, enkripsi komunikasi, transaksi digital, dan tanda tangan elektronik, menjadikannya dasar penting dalam perlindungan informasi di era digital.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 — Membuat Skema Kriptosistem
Buat diagram sederhana (bisa pakai draw.io, excalidraw, atau digambar lalu screenshot) dengan elemen:
Plaintext → [Algoritma + Kunci] → Ciphertext
Ciphertext → [Algoritma + Kunci] → Plaintext
Simpan diagram di folder screenshots/diagram_kriptosistem.png.
Lampirkan ke laporan menggunakan Markdown:
![Diagram Kriptosistem](screenshots/diagram_kriptosistem.png)

Langkah 2 — Implementasi Program Sederhana
Tulis program Python untuk simulasi enkripsi & dekripsi menggunakan substitusi sederhana (misalnya Caesar Cipher).

# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<nim><nama>"
    key = 5
    enc = encrypt(message, key)
    dec = decrypt(enc, key)
    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
    
Ekspektasi keluaran:

Plaintext : Cryptosystem Test
Ciphertext: Hwduytxzjxytr Yjxy
Decrypted : Cryptosystem Test

Langkah 3 — Klasifikasi Simetris & Asimetris
Tambahkan penjelasan di laporan mengenai perbedaan kriptografi simetris dan asimetris.
Sertakan minimal 1 contoh algoritma dari masing-masing:
Simetris → AES, DES
Asimetris → RSA, ECC

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:
---
```
def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "Cryptosystem Test"
    key = 5
    enc = encrypt(message, key)
    dec = decrypt(enc, key)
    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
```

Kriptografi simetris menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi. Metode ini cepat dan efisien, namun memiliki kelemahan dalam keamanan distribusi kunci.
Contoh algoritma: AES dan DES.

AES 
Contoh proses sederhana:
Plaintext (teks asli): HELLO1234567890
Kunci rahasia (key): MYSECRETKEY12345
Algoritma AES mengenkripsi plaintext menggunakan key tersebut.
Hasil Ciphertext (teks terenkripsi): A7D4F9C1B2E8


DES
Contoh proses sederhana:
Plaintext (teks asli): HELLO123
Kunci rahasia (key): MYSECRET
DES mengenkripsi teks dengan key melalui 16 tahap transformasi.
Ciphertext (hasil terenkripsi): 9F74A1B2C3D4E5F6



Sementara itu, kriptografi asimetris memakai dua kunci berbeda, yaitu kunci publik untuk mengenkripsi dan kunci privat untuk mendekripsi. Keunggulannya lebih aman dalam pertukaran kunci, tetapi prosesnya lebih lambat.
Contoh algoritma: RSA dan ECC.

RSA 
Contoh proses sederhana:
Plaintext (pesan asli): HELLO
Kunci publik: digunakan untuk mengenkripsi menjadi ciphertext → 5A9C2F...
Ciphertext: dikirim ke penerima
Kunci privat: digunakan penerima untuk mendekripsi dan mendapatkan kembali teks asli HELLO.


ECC
Contoh proses sederhana:
Plaintext (pesan asli): HELLO
Kunci publik (public key): digunakan untuk mengenkripsi pesan menjadi ciphertext → B8F3C9...
Ciphertext: dikirim ke penerima
Kunci privat (private key): digunakan penerima untuk mendekripsi dan mengembalikan pesan menjadi HELLO.

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
1. Komponen utama kriptosistem:

- Plaintext (pesan asli)
- Ciphertext (pesan terenkripsi)
- Algoritma enkripsi/dekripsi
- Kunci (key)
- Proses enkripsi dan dekripsi

2. Kelebihan dan kelemahan sistem simetris dibanding asimetris:
Kelebihan: proses enkripsi dan dekripsi lebih cepat, efisien untuk data besar.
Kelemahan: distribusi kunci tidak aman karena pengirim dan penerima harus memakai kunci yang sama.

3. Distribusi kunci jadi masalah utama karena:
Kunci harus dikirim ke pihak lain secara rahasia; jika kunci bocor saat dikirim, seluruh komunikasi bisa terbaca oleh pihak tidak berwenang.
---

## 8. Kesimpulan
Kriptosistem merupakan sistem yang digunakan untuk melindungi data melalui proses enkripsi dan dekripsi dengan bantuan algoritma serta kunci. Tujuannya adalah menjaga kerahasiaan, keaslian, dan integritas informasi agar tidak disalahgunakan oleh pihak yang tidak berwenang.

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
Author: Asadila Haila Hamada <asahamada255@gmail.com>
Date:   2025-10-14

    week2-cryptosystem: Cryposystem (Komponen, Enkripsi & Deskripsi, Simestris & Asimetris )
```
