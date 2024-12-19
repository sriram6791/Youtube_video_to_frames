# YouTube Frame Extractor

## Introduction

Tired of manually taking screenshots while watching lectures or any other videos on YouTube? This program is designed to automatically extract frames from a YouTube video based on the changes between consecutive frames—so you never miss a crucial moment!

## What Does This Program Do?

This tool allows you to:

- **Download YouTube Videos**: Just provide the URL of the YouTube video.
- **Automatically Extract Frames**: The program detects when there's a significant change between two frames and saves the new frame automatically. You won't have to worry about capturing frames yourself anymore!
- **Efficient Frame Detection**: Only significant frame changes are saved, avoiding repetitive or redundant frames.

## How to Use the Program

### 1. Install Required Libraries

Before you run the program, make sure to install the necessary dependencies. Open a terminal and run the following:

```bash
pip install opencv-python yt-dlp numpy scikit-image
```

These libraries are essential for downloading the video (`yt-dlp`), processing the video frames (`opencv-python`), performing image similarity analysis (`scikit-image`), and handling basic operations (`numpy`).

### 2. Download the YouTube Video

Once the required libraries are installed, you'll need to replace the YouTube video URL in the script. Find the line in the code:

```python
url = '_____YOUTUBE____LINK__HERE________'
```

Replace it with the URL of the YouTube video from which you want to extract frames.

### 3. Adjust the Similarity Threshold (Optional)

The program uses the **Structural Similarity Index (SSIM)** to compare frames and determine if they have significant differences. By default, the threshold is set at `0.96`, meaning that frames that are **96% similar or more** will not be saved.

If you find that too many or too few frames are being saved, you can adjust this threshold by modifying the following line:

```python
if similarity < 0.96:
```

- **Lowering the threshold** will save more frames (more sensitive to changes).
- **Increasing the threshold** will save fewer frames (only captures more noticeable changes).

### 4. Run the Program

After replacing the YouTube URL and optionally adjusting the threshold, simply run the Python script:

```bash
python script_name.py
```

Make sure you are in the correct directory where the script is located.

### 5. View the Saved Frames

Once the program has finished running, all the frames will be saved in a folder called `saved_frames` within your current directory. Each frame will be named with a timestamp of when it was extracted:

Example:

```
frame_1_1200.jpg
frame_2_1300.jpg
```

Each frame represents a significant change in the video.

## Additional Notes

- The video is **downloaded automatically** when you run the script. After downloading, the frames are processed.
- You can modify the program to save frames in different formats or perform additional actions (e.g., storing frames with custom names).
- This tool is especially useful for scenarios like **lecture capture**, **tutorial videos**, or **highlight reels**, where you only need to capture significant visual changes without manual intervention.

## Example Use Case

Imagine you're watching an online lecture and want to automatically capture key frames whenever something important happens. Instead of manually pausing and screenshotting, this tool automatically does it for you—saving time and effort!
```

This Markdown content is now fully formatted and ready for you to copy-paste into your `README.md` file. Let me know if you need further changes!
