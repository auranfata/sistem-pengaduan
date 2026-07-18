import tkinter as tk
from tkinter import messagebox

# ── Warna tema aplikasi (ubah di sini untuk ganti tema global) ──────────────
WARNA = {
    "primer":    "#1a3c5e",   # biru tua — header & tombol utama
    "sekunder":  "#2e86c1",   # biru sedang — aksen
    "aksen":     "#f39c12",   # oranye — highlight status
    "bg":        "#f0f4f8",   # abu sangat muda — background utama
    "putih":     "#ffffff",
    "teks":      "#2c3e50",
    "sukses":    "#27ae60",
    "bahaya":    "#e74c3c",
    "abu":       "#7f8c8d",
}

FONT = {
    "judul":   ("Segoe UI", 16, "bold"),
    "sub":     ("Segoe UI", 12, "bold"),
    "normal":  ("Segoe UI", 10),
    "kecil":   ("Segoe UI", 9),
}

STATUS_WARNA = {
    "Menunggu": "#f39c12",
    "Diproses": "#2980b9",
    "Selesai":  "#27ae60",
}


def tampil_pesan(judul: str, pesan: str, tipe: str = "info"):
    """Wrapper messagebox agar konsisten di seluruh View."""
    if tipe == "error":
        messagebox.showerror(judul, pesan)
    elif tipe == "warning":
        messagebox.showwarning(judul, pesan)
    else:
        messagebox.showinfo(judul, pesan)


def buat_tombol(parent, teks: str, perintah, warna_bg: str = None, lebar: int = 15):
    """Factory tombol dengan styling konsisten."""
    bg = warna_bg or WARNA["primer"]
    btn = tk.Button(
        parent,
        text=teks,
        command=perintah,
        bg=bg,
        fg=WARNA["putih"],
        font=FONT["normal"],
        width=lebar,
        relief="flat",
        cursor="hand2",
        padx=8,
        pady=4,
    )
    # Efek hover sederhana
    btn.bind("<Enter>", lambda e: btn.config(bg=WARNA["sekunder"]))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg))
    return btn


def buat_label_judul(parent, teks: str):
    """Label judul halaman yang seragam."""
    return tk.Label(
        parent,
        text=teks,
        font=FONT["judul"],
        bg=WARNA["primer"],
        fg=WARNA["putih"],
        pady=12,
    )


def tengahkan_window(window, lebar: int, tinggi: int):
    """Menempatkan window tepat di tengah layar."""
    window.update_idletasks()
    lyr_l = window.winfo_screenwidth()
    lyr_t = window.winfo_screenheight()
    x = (lyr_l - lebar) // 2
    y = (lyr_t - tinggi) // 2
    window.geometry(f"{lebar}x{tinggi}+{x}+{y}")
