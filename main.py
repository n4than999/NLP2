import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# === Import semua modul ===
from speak import speak
from listen import listen
from weather import get_weather
from schedule import get_schedule
from music import play_music
from datetime import datetime

# === Baca dataset intents ===
data = pd.read_csv("data/intents.csv")

texts = data["text"]
labels = data["label"]

# === Latih model Naive Bayes ===
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# === Fungsi prediksi intent ===
def predict_intent(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]

# === Fungsi utama untuk respon berdasarkan intent ===
def handle_intent(intent):
    if intent == "cuaca":
        response = get_weather()

    elif intent == "jadwal":
        jadwal = get_schedule()
        response = f"Berikut jadwal kamu hari ini: {jadwal}"

    elif intent == "salam":
        response = "Halo! Ada yang bisa saya bantu?"

    elif intent == "musik":
        response = "Baik, saya akan memutar musik."
        print(response)
        speak(response)
        play_music()
        return  # keluar agar tidak double speak di bawah

    elif intent == "waktu":
        now = datetime.now().strftime("%H:%M")
        response = f"Sekarang jam {now}"

    else:
        response = "Maaf, saya belum mengerti maksud kamu."

    print(response)
    speak(response)

# === Jalankan asisten ===
if __name__ == "__main__":
    speak("Hai, saya asisten kamu. Ucapkan sesuatu untuk memulai.")

    while True:
        kalimat = listen()  # Dengar suara pengguna
        if kalimat == "":
            continue

        # === Perintah keluar yang lebih fleksibel ===
        if any(kata in kalimat.lower() for kata in ["exit", "keluar", "quit", "stop", "bye", "sampai jumpa"]):
            speak("Sampai jumpa! Semoga harimu menyenangkan.")
            break

        # === Prediksi intent dan tangani ===
        intent = predict_intent(kalimat)
        print(f"🧠 Intent terdeteksi: {intent}")
        handle_intent(intent)
