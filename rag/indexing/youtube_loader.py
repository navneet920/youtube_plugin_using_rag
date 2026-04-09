from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriptLoader:
    def load_transcript(self, video_id: str) -> list[dict]:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)

        transcript = [
            {
                "text": item.text,
                "start": item.start,
                "duration": item.duration
            }
            for item in fetched
        ]

        return transcript