import openai
import pyaudio
import wave

openai.api_key = "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"

def listen_to_mic():
    # Set up the pyaudio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=1024)

    # Listen to the microphone until the user says "stop"
    print("Listening to microphone. Say 'stop' to stop.")
    audio_data = []
    while True:
        data = stream.read(1024)
        audio_data.append(data)
        result = openai.Completion.create(engine="davinci", prompt="Listening to microphone. Say 'stop' to stop. ", temperature=0.5, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0).get('choices')[0].get('text')
        if "stop" in result:
            break

    # Close the stream and write the audio data to a WAV file
    stream.stop_stream()
    stream.close()
    p.terminate()

    wav_file = wave.open("audio.wav", "wb")
    wav_file.setnchannels(1)
    wav_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wav_file.setframerate(16000)
    wav_file.writeframes(b''.join(audio_data))
    wav_file.close()

if __name__ == "__main__":
    listen_to_mic()

