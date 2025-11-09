import speech_recognition as sr
from speak import speak

def listen():
    """Mendengarkan input suara pengguna dan mengubahnya ke teks"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Asisten mendengarkan...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="id-ID")
        print("🗣️ Kamu bilang:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Maaf, saya tidak mendengar dengan jelas.")
        return ""
    except sr.RequestError:
        speak("Maaf, layanan suara sedang bermasalah.")
        return ""
