import os
import random
from gtts import gTTS
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from brain import get_automated_tip

def run_automation_cycle():
    tip_text = get_automated_tip()
    
    # Generate Audio
    tts = gTTS(text=tip_text, lang='en')
    tts.save("voice.mp3")
    audio = AudioFileClip("voice.mp3")

    # Pick a background video (Make sure you upload bg1.mp4 to GitHub!)
    video_file = "bg1.mp4"
    if os.path.exists(video_file):
        clip = VideoFileClip(video_file).subclip(0, audio.duration)
        final_video = clip.with_audio(audio)
        final_video.write_videofile("final_output.mp4", fps=24, codec="libx264")
        print("✅ Video Created! (Upload logic goes here)")
    else:
        print("❌ bg1.mp4 not found. Please upload a background video.")
