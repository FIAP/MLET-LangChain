from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=KKNCiRWd_j0",
    add_video_info=True,
    language=["pt", "id"],
    translation="pt",
)
result = loader.load()

print(result)