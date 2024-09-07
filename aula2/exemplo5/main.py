from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=rnp4HkIZWRk", add_video_info=False
)

result = loader.load()

print(result)