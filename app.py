import sounddevice as sd 
from scipy.io.wavfile import write 
from faster_whisper import WhisperModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from gtts import gTTS 

freq = 44100 
duration = 5 
device_id = 19 #Leads to default 


try:
    print("Recording...")
    record = sd.rec(int(duration * freq), samplerate=freq, channels=1, device=device_id)
    sd.wait()
    print("Finished.")
except Exception as e:
    print(f"Error: {e}")

write("record01.wav", freq, record)

#Config Faster-Whisper
model_size = "small"
model = WhisperModel(model_size, device="cpu", compute_type="float32")

segments, info = model.transcribe("record01.wav", beam_size=5)

for segment in segments:
    print("Got segment")
    transcription = segment.text
    print(transcription)

#Loading API Key 
load_dotenv() 

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
  model="google/gemma-3n-e2b-it:free",
  messages=[
    {
      "role": "user",
      "content": transcription
    }
  ]
)

ai_response = completion.choices[0].message.content

#Text-to-Speech output
gtts_obj = gTTS(text=ai_response, lang='pt', slow=False)

response_audio = "response_audio.wav"
gtts_obj.save(response_audio)

