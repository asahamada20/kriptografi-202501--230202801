import itertools
import string

def brute_force(charset, max_length, target):
    """
    Mencoba semua kombinasi password hingga max_length
    charset: karakter yang digunakan
    max_length: panjang maksimum password yang dicoba
    target: password yang ingin ditemukan
    """
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_str = ''.join(attempt)
            if attempt_str == target:
                return attempt_str
    return None

# Contoh penggunaan
charset = string.ascii_lowercase + string.digits  # karakter a-z dan 0-9
max_length = 4  # maksimal panjang password
target_password = "abc1"

found = brute_force(charset, max_length, target_password)

if found:
    print(f"Password ditemukan: {found}")
else:
    print("Password tidak ditemukan.")
