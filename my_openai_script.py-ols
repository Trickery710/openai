import pyaudio
import wave
import openai

# Set the OpenAI API key
openai.api_key = "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"

# Set the model ID
model_id = "YOUR_MODEL_ID"

# Set the audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

# Initialize PyAudio
p = pyaudio.PyAudio()

# Start recording
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("Recording...")
frames = []

for i in range(0, int(RATE / CHUNK
