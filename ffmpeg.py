import subprocess
import time
import os

start = time.time()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

frames_dir = os.path.join(BASE_DIR, "frames")

if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)
print(f"Frames folder path: {frames_dir}")

subprocess.run([
    "ffmpeg",
    "-i", "test.mp4",
    "-vf", "fps=1",
    "-q:v", "2",
    "frames/frame_%04d.jpg"
])

end = time.time()
print(f"Total time: {end - start:.2f} seconds")

