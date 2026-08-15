import whisper
# to run this project please download BtbN FFmpeg builds on GitHub (https://github.com/BtbN/FFmpeg-Builds/releases)
# and download it based on your Operating System. and then extract the file then
# all  the files inside BIN file copy them and paste them inside
# Introduction_to_OpenAI_Whipser package
model = whisper.load_model("base")
# Audio from Elden ring boss fight Margit
result =model.transcribe("audio-test.m4a")

print("Output: ", result["text"])
