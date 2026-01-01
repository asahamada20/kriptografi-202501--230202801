# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern (AES, RSA, DES)
Nama: Asadila Haila Hamada  
NIM: 230202801 
Kelas: 5 IKRA

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
Kriptografi modern menggunakan algoritma matematis yang kuat untuk menjaga kerahasiaan dan integritas data, dengan dua jenis utama yaitu cipher simetris dan asimetris. DES adalah algoritma simetris lama dengan kunci pendek yang kini tidak lagi aman terhadap serangan brute-force. AES hadir sebagai pengganti dengan ukuran blok dan kunci yang lebih besar sehingga lebih aman dan efisien. Sementara itu, RSA merupakan algoritma asimetris yang memanfaatkan pasangan kunci publik dan privat, dengan keamanan yang bergantung pada sulitnya memfaktorkan bilangan besar, dan umum digunakan untuk pertukaran kunci serta tanda tangan digital.

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


```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)# contoh potongan kode
def encrypt(text, key):
    return ...
```
```
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
```
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
)

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
1. Perbedaan DES, AES, dan RSA dalam kunci dan keamanan
DES dan AES adalah algoritma simetris yang menggunakan satu kunci yang sama untuk enkripsi dan dekripsi, namun DES memiliki kunci yang pendek sehingga kurang aman, sedangkan AES memiliki ukuran kunci yang lebih besar dan tingkat keamanan lebih tinggi. RSA berbeda karena bersifat asimetris, menggunakan sepasang kunci publik dan privat, dengan keamanan yang bergantung pada kesulitan faktorisasi bilangan besar.

2. Alasan AES lebih banyak digunakan daripada DES
AES lebih banyak digunakan karena memiliki ukuran kunci dan blok yang lebih besar, lebih tahan terhadap serangan brute-force, serta lebih efisien dan aman untuk kebutuhan kriptografi modern.

3. Alasan RSA disebut algoritma asimetris dan proses pembangkitan kunci
RSA disebut asimetris karena menggunakan dua kunci yang berbeda, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Kunci dibangkitkan dengan memilih dua bilangan prima besar, menghitung hasil perkaliannya, lalu membentuk pasangan kunci berdasarkan sifat matematika dari bilangan tersebut.
---

## 8. Kesimpulan
Melalui praktikum ini, mahasiswa dapat memahami perbedaan algoritma kriptografi simetris dan asimetris. Penerapan AES dan RSA dengan library PyCryptodome berjalan dengan baik, di mana AES efektif untuk pengamanan data, sedangkan RSA lebih sesuai untuk menjaga keamanan komunikasi dan pertukaran kunci.

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
