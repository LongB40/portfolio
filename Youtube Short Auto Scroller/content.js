const pattern = /[a-zA-Z]\w{10}/;

// Send message to background script with current URL when the page is loaded or when the URL changes
function sendUrlMessage() {
  const currentUrl = window.location.href;
  chrome.runtime.sendMessage({ url: currentUrl });
}

// Get video duration using YouTube API and scroll to the end of the video
function getVideoDuration(videoId) {
  const apiKey = 'AIzaSyD6EN2lFucJRBM1Z2pFU5JYYGSEL-XbSiw';
  fetch(`https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=${videoId}&key=${apiKey}`)
    .then(response => response.json())
    .then(data => {
      // add an event listener to check if the video has ended then send a keydown stroke
      console.log(videoId)
      const videoPlayer = document.querySelector('video');
      videoPlayer.addEventListener('ended', () => {
        simulateDownKey();
      });
    })
    .catch(error => console.error(error));
}

function simulateDownKey() {
  const downKeyCode = 40;
  const event = new KeyboardEvent('keydown', { keyCode: downKeyCode });
  document.dispatchEvent(event);
}

// Send message to background script with current URL when the page is loaded or when the URL changes
sendUrlMessage();
window.addEventListener('hashchange', sendUrlMessage);
