"""
controllers/pengaduan_controller.py
-------------------------------------
KONTRIBUTOR : Anggota C
BRANCH      : feature/pengaduan-controller
TUGAS       : Logika bisnis untuk operasi pengaduan
"""

from models.pengaduan_model import (
    buat_pengaduan,
    ambil_pengaduan_by_user,
    ambil_semua_pengaduan,
    ambil_detail_pengaduan,
    update_status_pengaduan,
    hapus_pengaduan,
)

KATEGORI_VALID = ["Infrastruktur", "Kebersihan", "Keamanan", "Pelayanan Publik", "Lainnya"]
STATUS_VALID   = ["Menunggu", "Diproses", "Selesai"]


def kirim_pengaduan(user_id: int, judul: str, deskripsi: str, kategori: str):
    """
    Warga mengirimkan pengaduan baru.
    Return: (True, pesan) atau (False, pesan_error)
    """
    if not judul.strip() or not deskripsi.strip():
        return False, "Judul dan deskripsi tidak boleh kosong."

    if len(judul) > 100:
        return False, "Judul maksimal 100 karakter."

    if kategori not in KATEGORI_VALID:
        return False, f"Kategori tidak valid. Pilih: {', '.join(KATEGORI_VALID)}"

    buat_pengaduan(user_id, judul.strip(), deskripsi.strip(), kategori)
    return True, "Pengaduan berhasil dikirim!"


def get_pengaduan_warga(user_id: int):
    """Mengambil daftar pengaduan milik warga tertentu."""
    return ambil_pengaduan_by_user(user_id)


def get_semua_pengaduan():
    """Mengambil semua pengaduan (dipakai oleh admin)."""
    return ambil_semua_pengaduan()


def get_detail(pengaduan_id: int):
    """Mengambil detail satu pengaduan."""
    return ambil_detail_pengaduan(pengaduan_id)


def ubah_status(pengaduan_id: int, status_baru: str):
    """
    Admin mengubah status pengaduan.
    Return: (True, pesan) atau (False, pesan_error)
    """
    if status_baru not in STATUS_VALID:
        return False, f"Status tidak valid. Pilih: {', '.join(STATUS_VALID)}"

    update_status_pengaduan(pengaduan_id, status_baru)
    return True, f"Status diubah menjadi '{status_baru}'."


def hapus(pengaduan_id: int):
    """Admin menghapus pengaduan."""
    hapus_pengaduan(pengaduan_id)
    return True, "Pengaduan berhasil dihapus."
