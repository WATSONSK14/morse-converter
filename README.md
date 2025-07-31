# Morse Code Converter 🔤

This is a basic Python project that converts English letters into Morse code. The project has two versions: a terminal-based (IDE) version and a simple Flask web version.

## 🔧 Project Structure

```
Morse Converter/
│
├── Flask/
│   ├── app.py
│   ├── templates/
│   │   └── home.html
│   └── static/ (optional)
│
├── IDE/
│   └── morse_converter.py
│
├── morse_alphabet.json
└── README.md
```

## 📦 Requirements

Only `Flask` is required for the web version.

You can install it with:

```bash
pip install Flask
```

Or, generate all dependencies using:

```bash
pipreqs . --force
```

## 🚀 How to Run

### IDE Version

```bash
python morse_converter.py
```

### Flask Version

```bash
cd Flask
python app.py
```

⚠️ For development only. Do not use `debug=True` in production.

Then open `http://127.0.0.1:5000/` in your browser.

## 🌍 Turkish Explanation

Bu proje, girilen bir metni Mors alfabesine çeviren basit bir Python uygulamasıdır. Hem konsol üzerinden çalışan versiyonu hem de web arayüzü (Flask ile) vardır.

- `morse_alphabet.json` dosyası Mors alfabesini tutar.
- Web versiyonunda kullanıcı arayüzü sade bir HTML ile sunulur.
- Geçersiz karakterler için uyarı verir.

## 📄 License

MIT License

---

**Author:** Serhat Kutlu (watsonsk14)(https://github.com/WATSONSK14)  
**Repository:** [morse-converter](https://github.com/WATSONSK14/morse-converter)
