from sqlalchemy.orm import Session
from models.model import Mahasiswa


class MahasiswaRepository:

    def __init__(self, db_session: Session):
        self.db = db_session

    def simpan_data(self, nama: str, ipk: float, sks: int, status: str) -> Mahasiswa:

        # Membuat data mahasiswa baru
        data_baru = Mahasiswa(
            nama=nama,
            ipk=ipk,
            sks=sks,
            status_kelulusan=status
        )

        # Menyimpan data ke database
        self.db.add(data_baru)
        self.db.commit()
        self.db.refresh(data_baru)

        return data_baru

    def ambil_semua_data(self):
        # Mengambil seluruh data mahasiswa
        return self.db.query(Mahasiswa).all()