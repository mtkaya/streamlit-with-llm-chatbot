# streamlit-with-llm-chatbot
Interactive chatbot using Streamlit and locally hosted LLMs (via Ollama) with FastAPI backend and Hugging Face deployment support.


# 🤖 Streamlit with LLM ChatBot

Bu proje, **Streamlit**, **FastAPI** ve **Ollama** kullanarak yerel olarak çalışan bir sohbet botu (chatbot) geliştirmeye yöneliktir. Arayüz kullanıcı dostu, hızlı ve farklı yerel modellerle (llama3, phi3, mistral) çalışacak şekilde tasarlanmıştır.

---

## 🎯 Amaç

- Yerel LLM’lerle çalışan bir chatbot geliştirmek  
- Modeller arası kolay geçiş ve kıyaslama  
- Hugging Face Spaces üzerinden dağıtılabilir bir yapı sağlamak

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji     | Açıklama                                  |
|---------------|--------------------------------------------|
| Streamlit     | Kullanıcı arayüzü için                    |
| FastAPI       | API katmanı için                          |
| Ollama        | Yerel LLM modellerini çalıştırmak için    |
| Python        | Tüm geliştirme için                       |
| Hugging Face  | Uygulamanın bulutta barındırılması için   |

---

## 📦 Gereksinimler


python>=3.8
ollama (kurulu ve modeller yüklenmiş olmalı)

## ⚙️ Kurulum

git clone https://github.com/kullanici-adin/streamlit-with-llm-chatbot.git
cd streamlit-with-llm-chatbot
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

##🚀 Kullanım

1. Ollama Modelini Başlat
ollama run llama3
2. FastAPI Server'ı Başlat
uvicorn api:app --reload --port 8000
3. Streamlit Arayüzünü Başlat
streamlit run app.py

## 📤 Hugging Face Spaces'e Yayınlama

Hugging Face hesabı oluştur.
Yeni bir Space aç: Tipi Streamlit olsun.
Bu 3 dosyayı yükle:
app.py
requirements.txt
README.md
Space otomatik olarak başlatılacaktır.

## 📁 Dosya Yapısı

```bash 
streamlit-with-llm-chatbot/
├── app.py              # Streamlit arayüzü
├── api.py              # FastAPI API servisi
├── requirements.txt    # Bağımlılıklar
├── README.md           # Proje tanıtımı
└── venv/               # Sanal ortam (push etme!)

## 📝 Geliştirme Notları

Şimdilik sadece llama3, phi3, mistral destekleniyor.
İlerleyen sürümlerde chat history, token sayacı, benchmark ve loglama eklenecek.
