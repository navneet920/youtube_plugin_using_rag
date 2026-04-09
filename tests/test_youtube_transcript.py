from services.youtube_service import YouTubeService

url = "https://www.youtube.com/watch?v=IDYXac1zOPw"

service = YouTubeService()
transcript = service.get_transcript_from_url(url)

for chunk in transcript[:5]:
    print(chunk)