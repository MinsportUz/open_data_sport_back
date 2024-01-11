from pytube import YouTube as yt


def youtube_video_stats(url):
    try:
        if not url:
            return 0
        video = yt(url)
        return video.views
    except Exception as e:
        print(e)
        return 0