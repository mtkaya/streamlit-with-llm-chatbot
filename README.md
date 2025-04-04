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

```bash
python>=3.8
ollama (kurulu ve modeller yüklenmiş olmalı)
