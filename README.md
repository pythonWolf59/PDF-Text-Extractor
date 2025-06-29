Here’s a polished and modern `README.md` file for your **PDF Label-Value Extractor** Streamlit app:

---

````markdown
# 📄 PDF Label-Value Extractor

A powerful Streamlit web app to extract values from custom-labeled text blocks across multiple PDF files — without relying on coordinates. Just specify a label and the direction (e.g., right, below), and this app does the rest!

![screenshot](https://placehold.co/1000x300?text=PDF+Label+Value+Extractor+App)

---

## ✨ Features

✅ Upload **multiple PDF files** (up to 50)  
✅ Specify the **label text** you want to extract (e.g., `Drawing / Specification ref:`)  
✅ Define the **direction** where the value appears (Right, Left, Above, or Below)  
✅ Supports **scanning a specific page** (e.g., Page 1 only)  
✅ Displays results per file in a clean output panel  
✅ **Download extracted values** as a `.txt` file

---

## 🧠 How It Works

1. **User uploads** one or more PDF files.
2. **App scans** the selected page from each PDF.
3. It searches for the **specified label** using fuzzy matching.
4. Then, it extracts the **closest matching value** in the selected direction.
5. Displays results in a clean list + downloadable format.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- Streamlit
- PyMuPDF (`fitz`)

### 💻 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/pdf-label-extractor.git
cd pdf-label-extractor

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
````

### 📦 Requirements.txt

```txt
streamlit
PyMuPDF
```

---

## 🚦 Usage

```bash
streamlit run app.py
```

1. Upload 1–50 PDF files.
2. Enter the **label text** (e.g., `CONTRACTOR INSPECTION REQUEST No.`)
3. Choose the direction of the value (`right`, `below`, etc.)
4. Set the page number to scan.
5. Click **"Extract Values"**
6. Copy or download the results as `.txt`.

---

## 💡 Example Use Cases

* Extract Drawing Numbers from Engineering PDFs
* Grab Serial Codes, Dates, or References across many files
* Bulk QA documentation parsing
* Custom data mining from industrial PDFs

---

## 🔐 Limitations & Notes

* Works best with **digitally generated PDFs** (not scanned images)
* Labels and values must be **text-based**, not embedded in images
* **Fuzzy matching** handles minor text differences (e.g., typos or extra colons)

---

## 👨‍💻 Author

**Humxa Zakir**
💬 Built with passion for automating PDF data extraction
📧 \[[humxazakir11@gmail.com](mailto:humxazakir11@gmail.com)]

---

## 🏷️ License

MIT License. Feel free to modify and share.

---

## ⭐️ Like this tool?

Give it a ⭐ on GitHub and share it with your team!

```

---