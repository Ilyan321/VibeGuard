# ✨ VibeGuard: An AI-Powered Content Moderation Engine

[![Hugging Face Demo](https://img.shields.io/badge/Spaces-Demo-blue?logo=huggingface&logoColor=white)](https://huggingface.co/spaces/Ilyan321/vibeguard)  
<!-- Add more badges above as needed (build, license, etc.) -->

---

**VibeGuard** is an automated Trust & Safety NLP pipeline, designed to instantly analyze text and categorize harmful behavior across multiple risk vectors in real time.

---

## 🚦 The Problem

Modern digital platforms scale rapidly, but traditional manual content moderation is:

- **Slow**
- **Expensive**
- **Emotionally taxing** for human moderators

As user-generated content grows, automated, real-time solutions are critical to maintain trust and safety **without sacrificing user experience**.

---

## 🛠️ The Technical Solution

VibeGuard leverages state-of-the-art NLP to automatically classify content for risk, with:

- **Base Model**: Fine-tuned `distilbert-base-uncased` (fast, lightweight inference)
- **Dataset**: [Jigsaw Toxic Comment Classification dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
- **Performance**: _86.67% Accuracy_ on the validation set

---

## 🌟 Key Features

- **Multi-Label Detection:** Evaluates text for multiple risk categories at once (not just binary toxic/not).
- **Targeted Categories:** Detects the following risk vectors:
    - Toxic
    - Severe Toxic
    - Obscene
    - Threat
    - Insult
    - Identity Hate
- **User-Friendly Dashboard:** Minimalist, dark-mode Streamlit web UI for rapid inference and testing.

---

## 💻 Tech Stack

- **Deep Learning:** PyTorch, Hugging Face Transformers, Datasets
- **Frontend:** Streamlit
- **Deployment:** Hugging Face Spaces

---

## 📁 Repository Structure

```
notebooks/
  └── VibeGuard_Training.ipynb   # Data prep, fine-tuning, and evaluation notebook
src/
  └── app.py                     # Streamlit dashboard frontend
requirements.txt                 # Dependency list
README.md                        # Project documentation (this file)
```

---

## 🚀 Try the Live Demo

Test VibeGuard instantly on [Hugging Face Spaces](https://huggingface.co/spaces/Ilyankhan69/vibeguard).

---

## 🖥️ How to Run Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/Ilyan321/VibeGuard-Toxicity-Detector.git
    cd VibeGuard-Toxicity-Detector
    ```

2. **(Recommended) Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # on Unix or Mac
    .\venv\Scripts\activate   # on Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**
    ```bash
    streamlit run src/app.py
    ```
    The app will open in your browser at [http://localhost:8501](http://localhost:8501).

---

## 📖 License

[MIT](LICENSE) &copy; Ilyan321  
_See the `LICENSE` file for more details._

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome! Please open issues or submit pull requests.

---

## 📬 Contact

Questions? Reach out via [GitHub Issues](https://github.com/Ilyan321/VibeGuard-Toxicity-Detector/issues).
