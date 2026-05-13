import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="VibeGuard ✨", page_icon="✨")
st.title("✨ VibeGuard: Toxicity Check")

# 1. Define the Human-Readable Mapping
id2label = {
    "LABEL_0": "Toxic",
    "LABEL_1": "Severe Toxic",
    "LABEL_2": "Obscene",
    "LABEL_3": "Threat",
    "LABEL_4": "Insult",
    "LABEL_5": "Identity Hate"
}

@st.cache_resource
def load_model():
    return pipeline("text-classification", model="Ilyankhan69/VibeGuard-Model", top_k=None)

classifier = load_model()
user_input = st.text_area("Type something to analyze:")

if st.button("Check the Vibe"):
    if user_input:
        with st.spinner("Translating AI math to human vibes..."):
            results = classifier(user_input)[0]
            
            # Create a nice layout for results
            st.subheader("Vibe Analysis Results:")
            
            for res in results:
                # Translate the label using our dictionary
                human_label = id2label.get(res['label'], res['label'])
                score_pct = res['score'] * 100
                
                # Show a progress bar: Red for high toxicity, Green for low
                bar_color = "red" if res['score'] > 0.5 else "green"
                st.write(f"**{human_label}**")
                st.progress(res['score'])
                st.write(f"Confidence: {score_pct:.2f}%")
                st.divider()


# --- FOOTER CODE ---
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #6b7280; /* Subtle grey color */
        text-align: center;
        padding: 10px;
        font-size: 12px;
        letter-spacing: 0.5px;
    }
    </style>
    <div class="footer">
        🚀 Personal Project by Ilyan khan | Fine-tuned DistilBERT | 86.67% Accuracy | Data: Jigsaw Toxicity
    </div>
    """, unsafe_allow_html=True)
