import os
import random
import sys
from pydub import AudioSegment
from pydub.effects import speedup

# --- CONFIGURATION ---
SOUND_FOLDER = "sounds"
OUTPUT_FOLDER = "outputs"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load clips from sounds/
sound_files = [os.path.join(SOUND_FOLDER, f) for f in os.listdir(SOUND_FOLDER) if f.endswith(".wav")]
clips = [AudioSegment.from_wav(f) for f in sound_files]

def distort_clip(base_clip, semitone_shift=0):
    """Pitch shift by semitone adjustment"""
    new_sample_rate = int(base_clip.frame_rate * (2.0 ** (semitone_shift / 12.0)))
    distorted = base_clip._spawn(base_clip.raw_data, overrides={'frame_rate': new_sample_rate})
    return distorted.set_frame_rate(44100)

def generate_talk_audio(text, filename="talk_output.wav", semitone_shift=0, speed=1.25):
    """Generate glitched typing sound and export as .wav"""
    print(f"🔊 Generating '{filename}' with pitch {semitone_shift} and speed {speed}x")

    output = AudioSegment.silent(duration=0)

    for char in text:
        if char.isalnum():
            clip = random.choice(clips)
            glitched = distort_clip(clip, semitone_shift)
            output += glitched + AudioSegment.silent(duration=15)

    output = speedup(output, playback_speed=speed)

    out_path = os.path.join(OUTPUT_FOLDER, filename)
    output.export(out_path, format="wav")
    print(f"✅ Exported: {out_path}")

# --- Command-line interface ---
if __name__ == "__main__":
    # Defaults
    text = "hello. this is default undertalk."
    filename = "talk_output.wav"
    pitch = 0
    speed = 1.25

    # Usage: python typingvoice.py "text here" filename.wav pitch speed
    if len(sys.argv) >= 2:
        text = sys.argv[1]
    if len(sys.argv) >= 3:
        filename = sys.argv[2]
    if len(sys.argv) >= 4:
        pitch = float(sys.argv[3])
    if len(sys.argv) >= 5:
        speed = float(sys.argv[4])

    generate_talk_audio(text, filename, pitch, speed)



