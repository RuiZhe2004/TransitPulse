"""TransitPulse dashboard served through Streamlit.

The dashboard itself is a self-contained HTML/JS page (transitpulse.html, map image embedded).
Streamlit only hosts it, so the page runs exactly as it does in a browser.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TransitPulse", page_icon="🚌", layout="wide")

# The dashboard scrolls inside its own frame (sidebar and top bar stay pinned), so the frame
# fills the window and Streamlit's own page scroll is switched off. One scroll bar remains.
st.markdown(
    """<style>
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {overflow: hidden !important}
    .block-container {padding: 0 !important; max-width: 100% !important}
    [data-testid="stHeader"], header, footer {display: none !important}
    iframe {position: fixed; inset: 0; width: 100vw !important; height: 100vh !important; border: 0; display: block}
    </style>""",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "transitpulse.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
