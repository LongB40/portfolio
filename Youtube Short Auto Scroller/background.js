chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.url) {
    const videoIdMatch = message.url.match(new RegExp(message.pattern));
    if (videoIdMatch) {
      const videoId = videoIdMatch[0];
      console.log(`Video URL detected: ${message.url}`);
      
      const apiKey = 'AIzaSyD6EN2lFucJRBM1Z2pFU5JYYGSEL-XbSiw';
      fetch(`https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=${videoId}&key=${apiKey}`)
        .then(response => response.json())
        .then(data => {
          // add an event listener to check if the video has ended then send a keydown stroke
          const videoPlayer = document.querySelector('video');
          videoPlayer.addEventListener('ended', () => {
            simulateDownKey();
          });
        })
        .catch(error => console.error(error));
    }
  }
});

function simulateDownKey() {
  const downKeyCode = 40;
  const event = new KeyboardEvent('keydown', { keyCode: downKeyCode });
  document.dispatchEvent(event);
}