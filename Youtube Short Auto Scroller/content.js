// Send message to background script with current URL when the page is loaded or when the URL changes
function sendUrlMessage() {
  const currentUrl = window.location.href;
  const pattern = '([a-zA-Z0-9_-]{11})$'
  chrome.runtime.sendMessage({ url: currentUrl, pattern: pattern});
}

// Send message to background script with current URL when the page is loaded or when the URL changes
sendUrlMessage();
window.addEventListener('hashchange', sendUrlMessage);
