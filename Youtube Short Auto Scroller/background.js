// Listen for messages from the background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.url) {
    const videoIdMatch = message.url.match(pattern);
    if (videoIdMatch) {
      const videoId = videoIdMatch[0];
      console.log(`Video URL detected: ${message.url}`);
      getVideoDuration(videoId);
    }
  }
});
