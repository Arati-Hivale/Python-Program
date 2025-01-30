from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)

        # Display video details
        print(f"\nTitle: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Length: {yt.length} seconds")
        print(f"Author: {yt.author}\n")

        # Get available streams (resolution options)
        print("Available video resolutions:")
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        for i, stream in enumerate(streams, start=1):
            print(f"{i}. {stream.resolution}")

        # User selects resolution
        choice = int(input("\nEnter the number of your preferred resolution: ")) - 1
        selected_stream = streams[choice]

        # Download the video
        print("\nDownloading video...")
        selected_stream.download()
        print("Download complete! Video saved in the current directory.")

    except Exception as e:
        print("Error:", e)

# Get YouTube URL from the user
video_url = input("Enter YouTube video URL: ")
download_video(video_url)
