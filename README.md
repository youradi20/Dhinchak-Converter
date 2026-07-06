# ⚡ Dhinchak Converter

A modern, lightweight, and user-friendly **Unit Converter Desktop Application** built using **Python** and **CustomTkinter**.

Dhinchak Converter provides a clean graphical interface for performing everyday unit conversions with history tracking and persistent storage support.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-green)
![License](https://img.shields.io/badge/License-AGPL--3.0-yellow)

---

# ✨ Features

### 🌡️ Temperature Converter
Convert between:

- Celsius ↔ Fahrenheit
- Celsius ↔ Kelvin
- Fahrenheit ↔ Kelvin

### 📏 Length Converter

- Inches ↔ Centimeters

### ⚖️ Weight Converter

- Grams ↔ Pounds

---

# 🚀 Additional Features

- 🎨 **Modern GUI Design**
  - Clean and minimal dark-themed interface
  - Built using CustomTkinter components

- 🔄 **Unit Swap**
  - Instantly switch between input and output units

- 💾 **Conversion History**
  - Automatically stores recent conversions
  - Saves last 10 conversions locally

- 📂 **JSON Storage**
  - Lightweight persistent storage system

- ⌨️ **Keyboard Support**
  - Press `Enter` to convert quickly

- 🛡️ **Input Validation**
  - Prevents invalid conversions and wrong inputs

---

# 📸 Application Preview

<p align="center">
  <img src="assets/Application Preview.png" width="600">
</p>

---

# 🛠️ Tech Stack

| Technology | Purpose |
|----------|----------|
| Python | Core programming language |
| CustomTkinter | GUI development |
| JSON | Data persistence |
| pathlib | File handling |

---

# 📌 File Overview


### main.py

Application starting point.

Responsibilities:

- Initializes the application
- Connects GUI with history system
- Starts main event loop


---

### gui.py

Handles the graphical interface.

Contains:

- Window design
- Buttons
- Input fields
- Events
- User interactions


---

### converter.py

Core conversion engine.

Contains:

- Temperature formulas
- Length formulas
- Weight formulas
- Conversion lookup system


---

### history.py

Handles persistent storage.

Contains:

- Loading history
- Saving conversions
- Clearing records

---

# ⚙️ Installation Guide


## 1. Clone Repository

```bash
git clone https://github.com/youradi20/Dhinchak-Converter.git
```

Move into project:

```bash
cd Dhinchak-Converter
```

---

## 2. Create Virtual Environment


### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```


### Linux / macOS

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python main.py
```

---

# 🧠 Working Flow

The application follows a simple modular architecture:

```
User Input

     ↓

CustomTkinter GUI

     ↓

Conversion Engine

     ↓

Result Display

     ↓

JSON History Storage
```

---

# ⌨️ Controls


| Action | Control |
|-|-|
| Convert Value | ⚡ Convert Button |
| Quick Convert | Press Enter |
| Swap Units | ⇅ Button |
| Remove History | Clear Button |

---

# 🔮 Future Improvements

Planned upgrades:

- ☀️ Light/Dark theme switch
- 🖼️ Custom icons and images
- 🔊 Voice output support
- 📤 Export conversion history
- 📦 Build executable application
- ➕ More unit categories

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository

2. Create your feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

You are free to use, modify, and distribute this software under the terms of the AGPL-3.0 license.

Any modified versions distributed or provided over a network must also make their source code available under the same license.

See the `LICENSE` file for complete license details.

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.

```
Built with ❤️ using Python
```
