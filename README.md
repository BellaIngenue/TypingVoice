# TypingVoice Audio Generator (CLI) for Devs 🥰

## General Information:

TypingVoice is a simple CLI generator of the sound system used for dialogues in games like Celeste and Undertale!

See it live at: https://bellaingenue.github.io/TypingVoice/

## Dependencies

- Python 3.10: Make sure you have the CORRECT Version, as Audioop no longer works with any others higher than 3.10. Download 3.10 here: https://www.python.org/downloads/release/python-3100/
  - Make sure to add it in the Environmental PATH
- Pip Installer: Makes life easier
- Pydub: Handles loading, editing, and exporting audio
- Ffmpeg OR Libav: For non-WAV files like MP3
  - If you’re only working with .wav, you don’t need FFmpeg — pydub works with raw .wav files out of the box.
- SimpleAudio: Live Playback (if desired)


## Commands and Examples:

### Installing Dependencies:

``py -3.10 -m pip install pydub simpleaudio``

### Code Examples:

INPUTS: (text, filename, pitch, speed)
DEFAULT INPUT:
- filename: talk_output.wav
- pitch: 0 (normal)
- speed: 1.25x

GEN EXAMPLE: ``py -3.10 typingvoice.py``

EXAMPLE: ``py -3.10 typingvoice.py "Don't you know how to greet a new pal?" sans_line.wav -2 1.5``

OUTPUT LOCATION: /outputs/talk_output.wav

## Why?

I'm a Game Developer (In Progress) and I wanted to make an easy way to convert random sounds to Undertale/Celeste sounding dialogue lines