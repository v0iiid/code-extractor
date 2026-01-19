# Code Extractor from Videos 

Automatically extracts code snippets from programming tutorial videos using **Python**, **FFmpeg**, and **OpenCV**.  
The pipeline converts a video into frames, filters frames likely containing code, and prepares them for OCR extraction.  

This project is **fully free**, offline, and designed for **10–20 minute coding tutorials**.

---

## Features

- Extract frames from video automatically using **FFmpeg**
- Detect frames that likely contain code using **OpenCV**
- Save filtered frames in a folder ready for OCR
- Cross-platform (Windows, Linux, macOS)
- Configurable frame rate and filtering thresholds
- Fully offline and free

---

## Todos

- [x] Convert Video to frames.
- [ ] Frames filtering using openCV (check weather frames have code or not)
Dark background + high edge density (text present) + presence of code symbols ({ } ( ) ; < >).
- [ ] OCR to extract text from the video.
- [ ] Using LLM to combine the code and then creating folder and files.
