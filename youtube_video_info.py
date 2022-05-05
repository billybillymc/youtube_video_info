import googleapiclient.discovery

dev_key = "" # insert API key here
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = dev_key)
request = youtube.videos().list(
    part = "snippet,contentDetails,statistics",
    id = "" # Insert YouTube video ID here.
)
response = request.execute()
print(response)