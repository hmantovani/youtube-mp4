from pytube import YouTube
import pyperclip
import os

def download_youtube_video(link, path='~/Downloads'):
    """
    Download a YouTube video using pytube.

    :param link: str, The URL of the YouTube video.
    :param path: str, The path where the video will be saved.
    :return: None
    """
    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Select the highest resolution stream of the video
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download(output_path=path)
        print(f"Video downloaded successfully: {video_stream.default_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Fetching link from clipboard...")
    video_link = pyperclip.paste()

    if "youtube.com" in video_link or "youtu.be" in video_link:
        print(f"Downloading video from: {video_link}")
        download_youtube_video(video_link)
    else:
        print("No valid YouTube link found in clipboard.")

if __name__ == "__main__":
    main()
