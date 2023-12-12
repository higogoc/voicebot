from openai import OpenAI

client = OpenAI(
  api_key="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"
)
# read record file
audio_file_path = '/seoi/Clinic/06_LLMs/01_AI-Assiatant/output.mp3'

audio_file = open(audio_file_path, "rb")

transcript  = client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format="text")


print(transcript)


