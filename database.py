import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "pengaduan.db")


def get_connection():
    """Mengembalikan koneksi SQLite. Dipanggil oleh Model."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # hasil query bisa diakses seperti dict
    return conn


def init_db():
    """
    Membuat semua tabel jika belum ada.
    Dipanggil SATU KALI saat aplikasi pertama dijalankan (dari main.py).
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Tabel pengguna (warga & admin)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nama        TEXT    NOT NULL,
            username    TEXT    NOT NULL UNIQUE,
            password    TEXT    NOT NULL,
            role        TEXT    NOT NULL DEFAULT 'warga',  -- 'warga' atau 'admin'
            created_at  TEXT    DEFAULT (datetime('now','localtime'))
        )
    """)

    # Tabel pengaduan
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pengaduan (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL,
            judul       TEXT    NOT NULL,
            deskripsi   TEXT    NOT NULL,
            kategori    TEXT    NOT NULL,
            status      TEXT    NOT NULL DEFAULT 'Menunggu',  -- Menunggu / Diproses / Selesai
            tanggal     TEXT    DEFAULT (datetime('now','localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Seed akun admin default (jika belum ada)
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 'admin'")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO users (nama, username, password, role)
            VALUES ('Administrator', 'admin', 'admin123', 'admin')
        """)

    conn.commit()
    conn.close()
    print("[DB] Database siap.")
