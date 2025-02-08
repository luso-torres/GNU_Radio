from pydub import AudioSegment
from pathlib import Path

#File address.
input_file = Path('testfile.mp3')
output_file = Path('output.wav')

# Ensure ffmpeg is added to the system's PATH
AudioSegment.ffmpeg = 'C:/ffmpeg/bin/ffmpeg'  # Update with your ffmpeg path

# Load MP3 file
audio = AudioSegment.from_mp3(input_file)

# Export as WAV file
audio.export(output_file, format='wav')