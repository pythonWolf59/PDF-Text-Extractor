import streamlit as st
import fitz  # PyMuPDF
from typing import List

st.set_page_config(page_title="PDF Label-Value Extractor", layout="wide")
st.markdown("<h1 style='text-align: center;'>📄 PDF Label-Value Extractor</h1>", unsafe_allow_html=True)

# --- Helper Functions ---
def extract_all_blocks(pdf_bytes: bytes, page_number: int):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc.load_page(page_number)
    text_dict = page.get_text("dict")
    doc.close()

    blocks = []
    for block in text_dict["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                x, y = round(span["bbox"][0], 1), round(span["bbox"][1], 1)
                blocks.append({
                    "x": x,
                    "y": y,
                    "text": span["text"].strip()
                })
    return blocks

def find_label_value_pair(blocks: List[dict], label: str, direction: str) -> str:
    label_blocks = [b for b in blocks if label.lower() in b["text"].lower()]
    if not label_blocks:
        return "❌ Not found"

    label_block = label_blocks[0]
    lx, ly = label_block["x"], label_block["y"]

    candidates = []
    for b in blocks:
        bx, by = b["x"], b["y"]
        if direction == "right" and abs(by - ly) < 5 and bx > lx:
            candidates.append((bx, b["text"]))
        elif direction == "left" and abs(by - ly) < 5 and bx < lx:
            candidates.append((-bx, b["text"]))
        elif direction == "below" and abs(bx - lx) < 50 and by > ly:
            candidates.append((by, b["text"]))
        elif direction == "above" and abs(bx - lx) < 50 and by < ly:
            candidates.append((-by, b["text"]))

    if candidates:
        candidates.sort()
        return candidates[0][1]
    return "❌ Not found"


# --- Layout ---
st.markdown("### 📥 Upload PDF Files")
uploaded_files = st.file_uploader("Upload one or more PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")

    col1, col2 = st.columns([2, 1])
    with col1:
        label = st.text_input("🔍 Label Text to Search", "Drawing / Specification ref:")
        direction = st.selectbox("📐 Direction of Value", ["right", "left", "above", "below"])
    with col2:
        page_number = st.number_input("📄 Page Number", min_value=1, value=1)

    st.markdown("---")

    if st.button("🚀 Extract Values from PDFs"):
        st.info("Processing files. Please wait...")

        results = []
        for uploaded_file in uploaded_files:
            pdf_bytes = uploaded_file.read()
            try:
                blocks = extract_all_blocks(pdf_bytes, page_number - 1)
                value = find_label_value_pair(blocks, label, direction)
                results.append((uploaded_file.name, value))
            except Exception as e:
                results.append((uploaded_file.name, f"❌ Error: {str(e)}"))

        st.success("Extraction completed ✅")
        st.markdown("### 📤 Extracted Results")

        output_lines = []
        for fname, val in results:
            icon = "✅" if not val.startswith("❌") else "❌"
            st.markdown(f"""
                <div style="padding: 8px; margin-bottom: 10px; background-color: #f8f9fa; border-left: 4px solid #6366f1;">
                    <b>📁 {fname}</b><br>
                    <b>{label}:</b> <span style="color: {'green' if icon=='✅' else 'red'};">{val}</span>
                </div>
            """, unsafe_allow_html=True)
            output_lines.append(f"📁 {fname}\n{label}: {val}\n")

        st.download_button(
            "💾 Download Results as TXT",
            data="\n".join(output_lines),
            file_name="extracted_results.txt",
            mime="text/plain"
        )
