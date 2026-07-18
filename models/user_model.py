"""
models/user_model.py
--------------------
KONTRIBUTOR : Anggota B
BRANCH      : feature/auth
TUGAS       : Operasi database untuk tabel users (login, register)
"""

from database import get_connection


def cari_user_by_username(username: str):
    """Mencari satu user berdasarkan username. Return Row atau None."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


def buat_user(nama: str, username: str, password: str, role: str = "warga"):
    """
    Mendaftarkan user baru.
    Return True jika berhasil, False jika username sudah dipakai.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (nama, username, password, role) VALUES (?, ?, ?, ?)",
            (nama, username, password, role)
        )
        conn.commit()
        return True
    except Exception:
        return False  # username duplicate
    finally:
        conn.close()


def ambil_semua_user():
    """Mengambil semua user (untuk keperluan admin)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama, username, role, created_at FROM users")
    hasil = cursor.fetchall()
    conn.close()
    return hasil
