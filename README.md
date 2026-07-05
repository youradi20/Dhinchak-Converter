# ⚡ Dhinchak Converter

A clean, modern, and minimalist unit converter desktop application built with **Python** and **CustomTkinter**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🌡️ **Temperature Conversion**
  - Celsius ↔ Fahrenheit
  - Celsius ↔ Kelvin
  - Fahrenheit ↔ Kelvin

- 📏 **Length Conversion**
  - Inches ↔ Centimeters

- ⚖️ **Weight Conversion**
  - Grams ↔ Pounds

- 🌙 **Modern Dark Interface**
  - Clean and minimal GUI design

- 🔄 **Unit Swapping**
  - Swap source and target units instantly

- 🕘 **Conversion History**
  - Automatically saves the last 10 conversions
  - Uses JSON-based local storage

- ⌨️ **Keyboard Support**
  - Press `Enter` for quick conversion

- ⚠️ **Error Handling**
  - Handles invalid input and unsupported conversions gracefully


---

## 📸 Preview

```
⚡ Dhinchak Converter

🌡 Temperature | 📏 Length | ⚖ Weight

FROM:
[ 100 ] [ Celsius ▼ ]

          ⇅

TO:
[ 212 ] [ Fahrenheit ▼ ]

⚡ CONVERT


History:
100 Celsius → 212 Fahrenheit
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/youradi20/Dhinchak-Converter.git
```

Move into the folder:

```bash
cd Dhinchak-Converter
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python main.py
```

---

# 📁 Project Structure

```
Dhinchak-Converter/

│
├── main.py
│
├── gui.py
│
├── converter.py
│
├── history.py
│
├── history.json
│
├── requirements.txt
├── LICENSE
└── README.md
```

### File Responsibilities

| File | Purpose |
|-|-|
| `main.py` | Application entry point and module connection |
| `gui.py` | CustomTkinter interface and events |
| `converter.py` | Unit conversion functions and conversion logic |
| `history.py` | Handles saving/loading conversion history |
| `history.json` | Stores recent conversions |

---

# 🧠 How It Works

The application follows a modular structure:

```
User Input
     |
     v
CustomTkinter GUI
     |
     v
Converter Engine
     |
     v
Result Display
     |
     v
JSON History Storage
```

---

# 🛠️ Tech Stack

| Technology | Usage |
|-|-|
| Python | Core programming language |
| CustomTkinter | Modern desktop GUI |
| JSON | Persistent history storage |
| pathlib | File management |

---

# ⌨️ Controls

| Action | Control |
|-|-|
| Convert | `⚡ CONVERT` button |
| Quick Convert | Press `Enter` |
| Swap Units | `⇅` button |
| Clear History | `Clear` button |

---

# 🔮 Future Improvements

Planned features:

- ☀️ Light/Dark theme switch
- 🔊 Voice output support
- 📤 Export conversion report
- 🖼️ Custom icons and branding
- 📦 Executable application build

---

# 🤝 Contributing

Contributions and suggestions are welcome.

Feel free to:

- Fork this repository
- Create a new branch
- Submit a pull request

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

```
Made with ❤️ using Python
```
