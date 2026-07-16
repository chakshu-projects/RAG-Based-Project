import os
import subprocess

# print(os.listdir("tutorials"))
path = os.listdir("tutorials")
for i in path:
    title = os.path.splitext(i)[0]
    subprocess.run(["ffmpeg","-i",f"tutorials/{i}",f"audios/{title}.mp3"])
 
