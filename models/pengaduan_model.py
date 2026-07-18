"""
models/pengaduan_model.py
-------------------------
KONTRIBUTOR : Anggota A
BRANCH      : feature/pengaduan-model
TUGAS       : Operasi database untuk tabel pengaduan
"""

from database import get_connection


def buat_pengaduan(user_id: int, judul: str, deskripsi: str, kategori: str):
    """Menyimpan pengaduan baru ke database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pengaduan (user_id, judul, deskripsi, kategori)
        VALUES (?, ?, ?, ?)
    """, (user_id, judul, deskripsi, kategori))
    conn.commit()
    conn.close()


def ambil_pengaduan_by_user(user_id: int):
    """Mengambil semua pengaduan milik satu warga."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, p.judul, p.kategori, p.status, p.tanggal
        FROM pengaduan p
        WHERE p.user_id = ?
        ORDER BY p.tanggal DESC
    """, (user_id,))
    hasil = cursor.fetchall()
    conn.close()
    return hasil


def ambil_semua_pengaduan():
    """Mengambil semua pengaduan (untuk tampilan admin)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, u.nama, p.judul, p.kategori, p.status, p.tanggal
        FROM pengaduan p
        JOIN users u ON p.user_id = u.id
        ORDER BY p.tanggal DESC
    """)
    hasil = cursor.fetchall()
    conn.close()
    return hasil


def ambil_detail_pengaduan(pengaduan_id: int):
    """Mengambil detail lengkap satu pengaduan."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.*, u.nama AS nama_pelapor
        FROM pengaduan p
        JOIN users u ON p.user_id = u.id
        WHERE p.id = ?
    """, (pengaduan_id,))
    hasil = cursor.fetchone()
    conn.close()
    return hasil


def update_status_pengaduan(pengaduan_id: int, status_baru: str):
    """Admin mengubah status pengaduan."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE pengaduan SET status = ? WHERE id = ?",
        (status_baru, pengaduan_id)
    )
    conn.commit()
    conn.close()


def hapus_pengaduan(pengaduan_id: int):
    """Menghapus pengaduan dari database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pengaduan WHERE id = ?", (pengaduan_id,))
    conn.commit()
    conn.close()
