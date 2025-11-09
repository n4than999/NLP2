import pygame
import os
import random

def play_music(folder=r"C:\Users\Nanda\Music"):
    """Memutar musik acak dari folder lokal"""
    if not os.path.exists(folder):
        print("Folder musik tidak ditemukan:", folder)
        return

    # Ambil semua file mp3
    files = [f for f in os.listdir(folder) if f.endswith(".mp3")]
    if not files:
        print("Tidak ada file MP3 di folder:", folder)
        return

    # Pilih lagu secara acak
    song = random.choice(files)
    path = os.path.join(folder, song)

    print("🎶 Memutar:", song)

    # Inisialisasi pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    # Tunggu sampai musik selesai
    while pygame.mixer.music.get_busy():
        pass
