import edge_tts
import io
import pygame

# Fetch audio using Edge TTS
async def fetch_audio(text, voice="en-US-EricNeural", pitch='+0Hz', rate='+0%') -> bytes:
    try:
        communicate = edge_tts.Communicate(text, voice, pitch=pitch, rate=rate)
        audio_bytes = b""
        async for element in communicate.stream():
            if element["type"] == 'audio':
                audio_bytes += element["data"]
        return audio_bytes
    except Exception as e:
        print(f"Error in voice synthesis: {e}")
        return b""

# Play the synthesized audio
class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.channel = None
        self.sound = None
        self.volume = 1

    def play(self, audio_bytes: bytes) -> None:
        audio_file = io.BytesIO(audio_bytes)
        self.sound = pygame.mixer.Sound(audio_file)

        if self.channel and self.channel.get_busy():
            self.channel.stop()

        self.channel = self.sound.play()
        self.channel.set_volume(self.volume)

    def stop(self) -> None:
        if self.channel and self.channel.get_busy():
            self.channel.stop()

# Convert text to speech and play it
async def speak_text(text: str, voice="en-US-EricNeural") -> None:
    player = AudioPlayer()
    audio_bytes = await fetch_audio(text, voice)
    player.play(audio_bytes)
