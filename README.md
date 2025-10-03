# InstaPaglu - Instagram Downloader

A simple, modern, and responsive web app to download public Instagram content by link.

---

## Features
- **Download Multiple Media Types:** Paste an Instagram link to download Videos, Photos, Reels, and IGTV.
- **Simple Interface:** Clean and minimal UI built with HTML and Tailwind CSS.
- **Python Backend:** A robust backend powered by Python and FastAPI.
- **Temporary Storage:** All downloaded files are automatically deleted from the server after 1 hour.
- **Error Handling:** Clear feedback for invalid links or private content.
- **SEO Optimized:** Basic on-page SEO implemented for better search engine visibility.

---

## Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/gogi2811/instapaglu.git
cd instapaglu
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the server
```bash
python server.py
```

- The application will be available at [http://localhost:3000](http://localhost:3000).
- Open the URL in your browser to use the downloader.

---

## Project Structure
```
instapaglu/
├── public/
│   ├── index.html      # Main frontend UI
│   ├── main.js         # Frontend logic
│   └── logo.svg        # Application logo
├── server.py           # FastAPI backend
├── insta_downloader.py # Media download logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # This file
```

---

## SEO Enhancements
This project includes several on-page SEO improvements to help with search engine ranking:
- **Descriptive Title:** The HTML title is optimized for clarity and keywords.
- **Meta Tags:** Includes `description` and `keywords` meta tags to provide more context to search engines.
- **Semantic HTML:** The page structure uses semantic tags like `<main>`, `<header>`, and `<footer>`.
- **Image Alt Text:** The logo image has descriptive alt text.

---

## Disclaimer
> This tool is for personal use only. It is not affiliated with Instagram or Meta. Please respect Instagram’s terms of service and copyright laws when downloading and using content.

---

## License
MIT