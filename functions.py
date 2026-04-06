import requests
import subprocess
import json
import os

output = r"Downloads"

format_options_v = ["bv", "wv"]
format_options_a = ["ba", "wa"]

audio_type = ["mp3", "wav"]

video_command = ['yt-dlp', "-f", "bestvideo+bestaudio/best", "--recode-video", "mp4", "--js-runtimes", r"deno:C:\Users\benco\.deno\bin\deno.exe", "--console-title", "-o", f"{output}\\mp4\\%(title)s - %(uploader|Unknown)s.%(ext)s"]
audio_command = ["yt-dlp.exe","-x", "--console-title"]

def check_playlist(url, command):
    if "&list" in url:
        playlist_input = input("This link appears to contain a playlist. Would you like to download the full playlist? [y\\n]")
    if playlist_input.lower() == "n":
        command.append("--no-playlist")
        command.append(url)
        return command
    else:
        command.append("--yes-playlist")
        command.append(url)
        return command
    
def check_type():
    while True:
        for i, formats in enumerate(audio_type):
            print(f"{i}. {formats}")
        try: 
            option = int(input("Select audio format: "))
            
            if option > len(audio_type):
                print("Please input a value only within the list.")
            else:
                return option
            print("Invalid choice.")
        except ValueError:
            print("Make sure you're entering an int value.")

def download_video(url: str):
    command = check_playlist(url, video_command)
    
    try: 
        subprocess.run(command, check=True, text=True)
        print("Video downloaded!")
        return ""
    except subprocess.CalledProcessError as e:
        print(f"There was an error running the script. Please try again: {e.returncode}: {e.stderr}")
    except KeyboardInterrupt:
        print("Operation canceled by user.")
        return ""

def download_audio(url: str):
    #checking to see if the user wants to download the full playlist
    command = check_playlist(url, audio_command)
    #audio_format will be decided then thrown into the if statements below
    audio_format = check_type()

    try:
        if audio_format == 1:
            subprocess.run(command+["--audio-format", audio_type[audio_format], "-o", f"{output}\\{audio_type[audio_format]}\\%(title)s - %(uploader|Unknown)s.%(ext)s"], check=True, text=True)
        else:
            #--embed-thumbnail
            subprocess.run(command+["--audio-format", audio_type[audio_format], "--embed-thumbnail", "-o", f"{output}\\{audio_type[audio_format]}\\%(title)s - %(uploader|Unknown)s.%(ext)s"], check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"No video was found under this link.\n{e.returncode}: {e.stderr}")
        return ""
    except KeyboardInterrupt:
        print("Operation canceled by user.")
        return ""

if __name__ == "__main__":
    download_audio("https://youtu.be/FuX5_OWObA0?si=iiZCvWHNl8K6xrng")