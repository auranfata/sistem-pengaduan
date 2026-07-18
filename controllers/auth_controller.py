from models.user_model import cari_user_by_username, buat_user


def login(username: str, password: str):
    """
    Memvalidasi kredensial pengguna.
    Return: dict user jika berhasil, None jika gagal.
    """
    if not username or not password:
        return None, "Username dan password tidak boleh kosong."

    user = cari_user_by_username(username)

    if user is None:
        return None, "Username tidak ditemukan."

    if user["password"] != password:
        return None, "Password salah."

    # Ubah Row ke dict biasa agar mudah dipakai di View
    return dict(user), None


def register(nama: str, username: str, password: str, konfirmasi: str):
    """
    Memproses pendaftaran akun warga baru.
    Return: (True, pesan) atau (False, pesan_error)
    """
    if not nama or not username or not password:
        return False, "Semua field harus diisi."

    if len(password) < 6:
        return False, "Password minimal 6 karakter."

    if password != konfirmasi:
        return False, "Password dan konfirmasi tidak cocok."

    if cari_user_by_username(username):
        return False, "Username sudah digunakan."

    berhasil = buat_user(nama, username, password, role="warga")

    if berhasil:
        return True, "Akun berhasil dibuat. Silakan login."
    else:
        return False, "Gagal membuat akun. Coba lagi."
