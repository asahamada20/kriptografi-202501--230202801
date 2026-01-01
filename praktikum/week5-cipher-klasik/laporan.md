# Laporan Praktikum Kriptografi
Minggu ke-: 5 
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Asadila Haila Hamada
NIM: 230202801 
Kelas: 5 IKRA

---

## 1. Tujuan
Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
Mengimplementasikan algoritma transposisi sederhana.
Menjelaskan kelemahan algoritma kriptografi klasik dalam konteks keamanan modern.

---

## 2. Dasar Teori
Cipher klasik adalah teknik kriptografi awal yang digunakan untuk menyamarkan pesan dengan cara mengganti huruf (substitusi) atau menyusun ulang huruf (transposisi). Contoh substitusi cipher adalah Caesar Cipher, yang menggeser huruf sejauh nilai kunci tertentu dengan bantuan aritmetika modular, serta Vigenère Cipher yang menggunakan kata kunci sehingga pergeseran huruf menjadi lebih bervariasi dan lebih sulit dipecahkan. Sementara itu, Transposisi Cipher hanya mengubah urutan huruf tanpa menggantinya. Meskipun metode-metode ini efektif pada masanya, cipher klasik umumnya lemah terhadap kemampuan analisis dan komputasi modern.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  


Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
1. Kelemahan Caesar dan Vigenère Cipher
Caesar Cipher sangat lemah karena jumlah kuncinya terbatas, sedangkan Vigenère Cipher meskipun lebih kuat tetap dapat dipecahkan jika kuncinya pendek atau berulang.

2. Analisis frekuensi pada cipher klasik
Cipher klasik mudah diserang karena pola frekuensi huruf bahasa asli masih tampak pada ciphertext.

3. Substitusi vs Transposisi
Cipher substitusi mudah digunakan tetapi lemah karena frekuensi huruf tetap terlihat, sementara cipher transposisi lebih menyamarkan frekuensi namun masih rentan terhadap analisis pola dan posisi huruf.
)
---

## 8. Kesimpulan
Praktikum ini membahas dasar kriptografi klasik dengan menerapkan Caesar, Vigenère, dan Transposisi Cipher. Meskipun semua metode dapat mengenkripsi dan mendekripsi pesan dengan baik, cipher klasik dinilai tidak aman untuk penggunaan modern karena rentan terhadap brute-force dan analisis frekuensi.

---

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson. Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography. CRC Press. Singh, S. (1999). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography.

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
