import json
import os

def get_schedule():
    path = os.path.join("data", "schedule.json")
    if not os.path.exists(path):
        return "File jadwal tidak ditemukan."

    with open(path, "r", encoding="utf-8") as f:
        try:
            jadwal = json.load(f)
        except json.JSONDecodeError:
            return "Format file jadwal salah. Pastikan file JSON valid."

    hasil_list = []
    for hari, kegiatan in jadwal.items():
        kegiatan_hari = ", ".join(kegiatan)
        hasil_list.append(f"{hari}: {kegiatan_hari}")

    hasil = "Berikut jadwal kamu: " + ". ".join(hasil_list) + "."
    return hasil
