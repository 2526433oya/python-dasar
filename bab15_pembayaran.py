from abc import ABC, abstractmethod


class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass


class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")


class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")


def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)


proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)
