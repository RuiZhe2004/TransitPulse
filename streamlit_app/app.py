"""TransitPulse dashboard served through Streamlit.

The dashboard itself is a self-contained HTML/JS page (transitpulse.html, map image embedded).
Streamlit only hosts it, so the page runs exactly as it does in a browser.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TransitPulse", page_icon="🚌", layout="wide")

st.markdown(
    "<style>.block-container{padding:0.5rem 0.5rem 0;max-width:100%} header, footer{visibility:hidden}</style>",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "transitpulse.html").read_text(encoding="utf-8")
components.html(html, height=1500, scrolling=True)
