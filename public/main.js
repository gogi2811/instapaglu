const form = document.getElementById('downloadForm');
const urlInput = document.getElementById('instaUrl');
const errorMsg = document.getElementById('errorMsg');
const successMsg = document.getElementById('successMsg');
const spinner = document.getElementById('spinner');

function validateInstagramUrl(url) {
  return /^https:\/\/(www\.)?instagram\.com\/.+/.test(url);
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  errorMsg.textContent = '';
  successMsg.innerHTML = '';
  spinner.classList.add('flex');
  spinner.classList.remove('hidden');

  const url = urlInput.value.trim();
  if (!validateInstagramUrl(url)) {
    spinner.classList.add('hidden');
    spinner.classList.remove('flex');
    errorMsg.textContent = 'Please enter a valid Instagram video link.';
    return;
  }

  try {
    const response = await fetch('/download', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    spinner.classList.add('hidden');
    spinner.classList.remove('flex');
    if (response.ok) {
      const { downloadUrl } = await response.json();
      successMsg.innerHTML = `<a href="${downloadUrl}" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition" download="instagram_video.mp4">Download Video</a>`;
    } else {
      const { error } = await response.json();
      errorMsg.textContent = error || 'This video cannot be downloaded.';
    }
  } catch (err) {
    spinner.classList.add('hidden');
    spinner.classList.remove('flex');
    errorMsg.textContent = 'Server error. Please try again later.';
  }
});
