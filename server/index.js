const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const { downloadInstagramVideo } = require('./instaDownloader');

const app = express();
const PORT = process.env.PORT || 3000;
const TMP_DIR = path.join(__dirname, 'tmp');

if (!fs.existsSync(TMP_DIR)) fs.mkdirSync(TMP_DIR);

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

// Serve downloaded videos
app.use('/videos', express.static(TMP_DIR));

// Download endpoint
app.post('/download', async (req, res) => {
  const { url } = req.body;
  if (!/^https:\/\/(www\.)?instagram\.com\/.+/.test(url)) {
    return res.status(400).json({ error: 'Please enter a valid Instagram video link.' });
  }
  try {
    const { filePath, fileName } = await downloadInstagramVideo(url, TMP_DIR);
    const downloadUrl = `/videos/${fileName}`;
    res.json({ downloadUrl });
  } catch (err) {
    res.status(400).json({ error: err.message || 'This video cannot be downloaded.' });
  }
});

// Cleanup old files (TTL: 1 hour)
setInterval(() => {
  const now = Date.now();
  fs.readdir(TMP_DIR, (err, files) => {
    if (err) return;
    files.forEach(file => {
      const filePath = path.join(TMP_DIR, file);
      fs.stat(filePath, (err, stats) => {
        if (!err && now - stats.mtimeMs > 60 * 60 * 1000) {
          fs.unlink(filePath, () => {});
        }
      });
    });
  });
}, 30 * 60 * 1000); // every 30 min

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
