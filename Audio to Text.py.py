import whisper
import json
import os

model = whisper.load_model("large-v2")

result = model.transcribe(audio="audios/Html_content.mp4.mp3",
                          language="hi",
                          task="translate")
print(result["text"])


chunk = []
for segment in result["segments"]:
    chunk.append({"number":1,"title":"Html_content.mp4.mp3",
                  "start":segment["start"],"end":segment["end"],
                  "text":segment["text"]})
    
chunk_with_meta = {"chunks":chunk, "text":result["text"]}

with open ("json_file/Html_content.json","w+") as f:
    json.dump(chunk_with_meta,f)