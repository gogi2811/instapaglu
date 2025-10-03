# Existing content or placeholder text that might be in the README

## New Content
# Instagram Video Downloader

A simple, modern, and responsive web app to download public Instagram videos by link.

---

## Features
- **Paste Instagram video link** and download the video as `.mp4`
- **Frontend:** HTML + Tailwind CSS, responsive, minimal UI
- **Backend:** Node.js + Express
- **No user data stored**; videos are deleted from the server after 1 hour
- **Clear error handling** for invalid, private, or unavailable videos
- **Disclaimer:** For personal use only. Respect Instagram’s terms of service

---

## How It Works
1. **User** pastes a public Instagram video link and clicks "Download"
2. **Frontend** validates the link and sends it to the backend
3. **Backend** fetches the video using `instagram-url-direct` and stores it temporarily
4. **Frontend** shows a "Download Video" button if successful, or an error message if not
5. **Video files** are auto-deleted after 1 hour

---

## Setup & Usage

### 1. Clone the repository
```bash
git clone https://github.com/gogi2811/instapaglu.git
cd instapaglu
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start the server
```bash
npm start
```

- The app runs on [http://localhost:3000](http://localhost:3000)
- Open in your browser and use the interface

---

## Project Structure
```
instapaglu/
├── public/
│   ├── index.html      # Main frontend UI
│   └── main.js         # Frontend logic (validation, fetch, UI states)
├── server/
│   ├── index.js        # Express backend
│   └── instaDownloader.js # Video download logic
├── package.json        # Node.js dependencies and scripts
└── README.md           # This file
```

---

## API
### POST `/download`
- **Body:** `{ url: "<instagram_video_url>" }`
- **Response:** `{ downloadUrl: "/videos/filename.mp4" }` on success, or `{ error: "..." }` on failure

---

## Limitations & Notes
- Only works for **public** Instagram videos (not stories, private, or IGTV)
- If Instagram changes its structure, the downloader may need updating
- No user data is stored; all files are deleted after 1 hour

---

## Disclaimer
> For personal use only. This tool is not affiliated with Instagram. Please respect Instagram’s terms of service and copyright laws.

---

## License
MIT
# instapaglu