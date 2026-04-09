from rag.indexing.youtube_loader import YouTubeTranscriptLoader
from utils.url_parser import extract_video_id


class YouTubeService:
    def __init__(self):
        self.loader = YouTubeTranscriptLoader()

    def get_transcript_from_url(self, url: str) -> list[dict]:
        video_id = extract_video_id(url)
        return self.loader.load_transcript(video_id)