import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# === Baca dataset dari file CSV ===
# (pastikan file intents.csv ada di folder "data")
data = pd.read_csv("data/intents.csv")

# Pisahkan teks dan label
texts = data["text"]
labels = data["label"]

# === Latih model dengan algoritma Naive Bayes ===
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# === Fungsi untuk memprediksi intent dari teks ===
def predict_intent(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]

# === (Opsional) Uji model langsung ===
if __name__ == "__main__":
    while True: 
        kalimat = input("Kamu: ")
        if kalimat.lower() in ["exit", "keluar", "quit"]:
            break
        intent = predict_intent(kalimat)
        print("Intent terdeteksi:", intent)
