import requests
import json

# Define your API key and the API endpoint URL
api_key = "AIzaSyD0L60t-xQaVI_G_ya8hxbF5_VeVSnZwCU"
api_endpoint = "https://www.googleapis.com/youtube/v3/videos"

# Define the parameters of your API request
params = {
    "key": api_key,
    "part": "snippet,contentDetails,statistics",
    "id": "XJf7Gj_itSg"
}

# Send the API request using the requests library
response = requests.get(api_endpoint, params=params)


    # Process the API response
if response.status_code == 200:
    # Successful API call
    data = response.json()
    # Extract the duration value from the API response
    print(json.dumps(data, sort_keys=True, indent=4))
    duration = data["items"][0]["contentDetails"]["duration"]
    print("Video duration: {}".format(duration))
else:
    # Error occurred, handle it appropriately
    print("Error occurred: {}".format(response.text))