import streamlit as st

st.title("📄 Report")
st.write(
    """
    Qui verrà generato un **riepilogo** scaricabile dei risultati:
    - input inseriti,
    - percentuale ed esito,
    - data/ora e versione del modello.
    """
)
from ui import render_footer
render_footer("Francesco Mantini", "https://www.linkedin.com/in/francesco-mantini-aa8828382/", "https://github.com/Francesco3105")

