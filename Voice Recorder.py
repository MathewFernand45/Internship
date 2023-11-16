import pygame
import sounddevice as sd
import numpy as np
import wavio
import time

def record_audio(filename, duration=5, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()
    print("Recording complete.")
    wavio.write(filename, audio_data, sample_rate, sampwidth=3)

    print(f"Audio saved as {filename}")

def play_audio(filename):
    pygame.init()
    pygame.mixer.init()
    

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    filename = "recorded_audio.wav"

    record_audio(filename)
    time.sleep(1)

    play_audio(filename)

if __name__ == "__main__":
    main()
