import os
import openai
import moviepy.editor as mp
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
WHISPER_ENGINE = os.getenv('WHISPER_ENGINE')
LANG = os.getenv('LANG')
ENCODING = os.getenv('ENCODING')

openai.api_key = OPENAI_API_KEY

def convert_mp4_to_mp3(mp4_file_path):
  wav_file_path = os.path.splitext(mp4_file_path)[0] + '.mp3'
  audio = mp.AudioFileClip(mp4_file_path)
  audio.write_audiofile(wav_file_path)
  return wav_file_path

def transcribe_audio(wav_file_path):
  with open(wav_file_path, 'rb') as audio_file:
    transcription = openai.Audio.transcribe(WHISPER_ENGINE, audio_file, language=LANG)

  return transcription.text

def save_transcription_to_file(transcription, output_file_path):
  with open(output_file_path, 'w', encoding=ENCODING) as f:
    f.write(transcription)

if __name__ == "__main__":
  mp4_file_path = input("Enter the path of mp4 file: ")
  wav_file_path = convert_mp4_to_mp3(mp4_file_path)

  transcription = transcribe_audio(wav_file_path)
  print("Audio transcription completed.")

  output_file_path = os.path.splitext(mp4_file_path)[0] + '_transcription.txt'
  save_transcription_to_file(transcription, output_file_path)
  print(f"The voice transcription result is saved to: {output_file_path}")
