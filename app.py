
# import streamlit as st
# import cv2
# import os
# import shutil
# from moviepy.editor import VideoFileClip
# import speech_recognition as sr
# from pydub import AudioSegment

# # Set folders
# FRAMES_DIR = "frames"
# AUDIO_DIR = "audio_text"

# # Create folders
# os.makedirs(FRAMES_DIR, exist_ok=True)
# os.makedirs(AUDIO_DIR, exist_ok=True)

# # Clean old files
# def clean_folders():
#     shutil.rmtree(FRAMES_DIR, ignore_errors=True)
#     shutil.rmtree(AUDIO_DIR, ignore_errors=True)
#     os.makedirs(FRAMES_DIR, exist_ok=True)
#     os.makedirs(AUDIO_DIR, exist_ok=True)

# # Streamlit UI
# st.set_page_config(page_title="Video Frame & Audio Text Extractor")
# st.title("🎬 Video Frame & Audio Text Extractor")
# st.markdown("Upload a short video file (10–20 seconds)")

# uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

# if uploaded_file:
#     with open("input_video.mp4", "wb") as f:
#         f.write(uploaded_file.read())
#     st.video("input_video.mp4")

#     if st.button("🚀 Process Video"):
#         clean_folders()

#         # Step 1: Extract Frames
#         cap = cv2.VideoCapture("input_video.mp4")
#         frame_count = 0
#         while True:
#             success, frame = cap.read()
#             if not success:
#                 break
#             frame_path = os.path.join(FRAMES_DIR, f"frame_{frame_count:04d}.jpg")
#             cv2.imwrite(frame_path, frame)
#             frame_count += 1
#         cap.release()
#         st.success(f"{frame_count} frames extracted and saved in 'frames/'")

#         # Step 2: Extract Audio
#         video_clip = VideoFileClip("input_video.mp4")
#         audio_path = os.path.join(AUDIO_DIR, "audio.wav")
#         video_clip.audio.write_audiofile(audio_path)

#         # Step 3: Convert Audio to Text
#         recognizer = sr.Recognizer()
#         audio = AudioSegment.from_wav(audio_path)
#         audio.export("temp.wav", format="wav")

#         with sr.AudioFile("temp.wav") as source:
#             audio_data = recognizer.record(source)
#             try:
#                 text = recognizer.recognize_google(audio_data, language="en-IN")
#                 text_path = os.path.join(AUDIO_DIR, "audio_text.txt")
#                 with open(text_path, "w", encoding="utf-8") as f:
#                     f.write(text)
#                 st.success("✅ Audio converted to text:")
#                 st.text_area("📄 Transcribed Text", text, height=200)
#                 st.download_button("📥 Download Text", text, file_name="audio_text.txt")
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

#         os.remove("temp.wav")


















import streamlit as st
import cv2
import os
import shutil
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

# Set folders
FRAMES_DIR = "frames"
AUDIO_DIR = "audio_text"

# Create folders
os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

# Clean old files
def clean_folders():
    shutil.rmtree(FRAMES_DIR, ignore_errors=True)
    shutil.rmtree(AUDIO_DIR, ignore_errors=True)
    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)

# Streamlit UI
st.set_page_config(page_title="Video Frame & Audio Text Extractor")
st.title("🎬 Video Frame & Audio Text Extractor")
st.markdown("Upload a short video file (10–20 seconds)")

uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

if uploaded_file:
    with open("input_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    st.video("input_video.mp4")

    if st.button("🚀 Process Video"):
        clean_folders()

        # Step 1: Extract Frames
        cap = cv2.VideoCapture("input_video.mp4")
        frame_count = 0
        while True:
            success, frame = cap.read()
            if not success:
                break
            frame_path = os.path.join(FRAMES_DIR, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        cap.release()
        st.success(f"{frame_count} frames extracted and saved in 'frames/'")

        # Step 1.1: Preview first 5 frames
        st.subheader("🖼️ Frame Preview")
        frame_files = sorted(os.listdir(FRAMES_DIR))[:5]
        for file in frame_files:
            frame_path = os.path.join(FRAMES_DIR, file)
            st.image(frame_path, caption=file, use_column_width=True)

        # Step 2: Extract Audio
        video_clip = VideoFileClip("input_video.mp4")
        audio_path = os.path.join(AUDIO_DIR, "audio.wav")
        video_clip.audio.write_audiofile(audio_path)

        # Step 3: Convert Audio to Text
        recognizer = sr.Recognizer()
        audio = AudioSegment.from_wav(audio_path)
        audio.export("temp.wav", format="wav")

        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language="en-IN")
                text_path = os.path.join(AUDIO_DIR, "audio_text.txt")
                with open(text_path, "w", encoding="utf-8") as f:
                    f.write(text)
                st.success("✅ Audio converted to text:")
                st.text_area("📄 Transcribed Text", text, height=200)
                st.download_button("📥 Download Text", text, file_name="audio_text.txt")
            except Exception as e:
                st.error(f"❌ Error: {e}")

        os.remove("temp.wav")
