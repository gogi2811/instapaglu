// Instagram video downloader logic
// Uses 'instagram-url-direct' for lightweight video extraction
const { getInfo } = require('instagram-url-direct');
const fs = require('fs');
const path = require('path');
const axios = require('axios');

async function downloadInstagramVideo(instaUrl, tmpDir) {
  try {
    const info = await getInfo(instaUrl);
    if (!info || !info.url_list || !info.url_list[0]) {
      throw new Error('This video cannot be downloaded.');
    }
    const videoUrl = info.url_list[0];
    const fileName = `instagram_video_${Date.now()}.mp4`;
    const filePath = path.join(tmpDir, fileName);
    const response = await axios({
      url: videoUrl,
      method: 'GET',
      responseType: 'stream',
    });
    await new Promise((resolve, reject) => {
      const stream = response.data.pipe(fs.createWriteStream(filePath));
      stream.on('finish', resolve);
      stream.on('error', reject);
    });
    return { filePath, fileName };
  } catch (err) {
    throw new Error('This video cannot be downloaded.');
  }
}

module.exports = { downloadInstagramVideo };
