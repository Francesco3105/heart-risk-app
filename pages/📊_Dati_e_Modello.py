import streamlit as st
from ml import train_logistic_regression_model


st.title("📊 Dati & Modello — Panoramica")
st.write(
    """
    In questa pagina verranno mostrati:
    - il dataset utilizzato (anteprima e descrizione colonne),
    - i passaggi di **pre‑processing** (pulizia, encoding, scaling),
    - il **modello** scelto per la classificazione (baseline).

    """
)

st.write(
    "Click the button to train a **binary** Logistic Regression on the OpenML heart dataset. "
    "The trained model will be stored in memory (session state) and used by the Simulator page."
)

train_button_clicked = st.button("Train model")

if train_button_clicked:
    try:
        info_msg = st.info("⏳ Training in progress… This may take a few seconds the first time (dataset download).")
        trained_model = train_logistic_regression_model()
        
        st.session_state["model"] = trained_model  # store for other pages
        info_msg.empty()  # Remove the info message
        st.success("✅ Model trained and stored in memory.")
        st.caption("LogisticRegression with default settings. No preprocessing, no pipeline.")
        
    except Exception as error:
        st.error(f"Training failed. Details: {error}")

# Status indicator (so students know if a model is available)
if "model" in st.session_state:
    st.success("A trained model is available in memory and ready to use in the Simulator page.")
else:
    st.warning("No model in memory yet. Click 'Train model' to create one.")



from ui import render_footer
render_footer("Francesco Mantini", "https://www.linkedin.com/in/francesco-mantini-aa8828382/", "https://github.com/Francesco3105")


