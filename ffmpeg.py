import subprocess
import time

start = time.time()

subprocess.run([
    "ffmpeg",
    "-i", "test.mp4",
    "-vf", "fps=1",
    "-q:v", "2",
    "frames/frame_%04d.jpg"
])

end = time.time()
print(f"Total time: {end - start:.2f} seconds")

