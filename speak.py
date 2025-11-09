import pyttsx3

def speak(text):
    """Fungsi untuk membuat asisten berbicara dengan benar (tidak eja huruf)"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Kecepatan bicara
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Bersihkan karakter yang bikin mesin eja huruf per huruf
    clean_text = text.replace("\n", " ").replace("\r", " ").strip()
    
    # Pastikan encoding aman
    try:
        clean_text = clean_text.encode('utf-8').decode('utf-8')
    except:
        pass

    engine.say(clean_text)
    engine.runAndWait()
    engine.stop()
