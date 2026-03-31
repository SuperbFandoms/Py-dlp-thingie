import subprocess
import functions as f
import os

options = {
    "1": "Download video",
    "2": "Download Audio",
    "3": "Options",
}
options_length = len(options)

if __name__ == "__main__":

    while True:
        for key, value in options.items():
            print(f"{key}. {value}")
        try:
            stream = input("Input option: (q to quit) ")
        
            match (stream):
                case("1"):
                    url = input("Input URL: ")
                    f.download_video(url)
                case("2"):
                    url = input("Input URL: ")
                    f.download_audio()
                case("3"):
                    pass
                case("q"):
                    exit()
                case _:
                    print("Invalid answer!")
        except ValueError as er:
            print(f"Please input an int value.)")

            
        
