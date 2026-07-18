import sys
import os

# Tambah root project ke sys.path agar semua import berjalan
sys.path.insert(0, os.path.dirname(__file__))

from database import init_db
from views.login_view import LoginView
from views.dashboard_view import DashboardView


def on_login_sukses(user: dict):
    """Callback dipanggil LoginView saat login berhasil."""
    DashboardView(user).mainloop()


if __name__ == "__main__":
    # 1. Siapkan database
    init_db()

    # 2. Tampilkan halaman login
    LoginView(on_login_sukses).mainloop()
