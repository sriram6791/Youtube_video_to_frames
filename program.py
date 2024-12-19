import cv2
import numpy as np
import yt_dlp
import os
from skimage.metrics import structural_similarity as ssim

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.mp4',
        'format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def frame_similarity(prev_frame, curr_frame):
    # Convert frames to grayscale
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
    
    # Compute SSIM
    score, _ = ssim(prev_gray, curr_gray, full=True)
    return score

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    saved_count = 0
    prev_frame = None
    
    # Create a folder to save the frames
    save_folder = 'saved_frames'
    os.makedirs(save_folder, exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if prev_frame is None:
            prev_frame = frame
            continue

        # Compute similarity between the current frame and the previous frame
        similarity = frame_similarity(prev_frame, frame)

        # If similarity is below the threshold, consider it a new frame
        if similarity < 0.96:  # You may need to adjust this threshold
            saved_count += 1
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
            filename = os.path.join(save_folder, f'frame_{saved_count}_{timestamp:.0f}.jpg')
            cv2.imwrite(filename, frame)
            print(f'Saved {filename}')

        prev_frame = frame
        frame_count += 1

    cap.release()
    print(f'Total frames processed: {frame_count}')
    print(f'Total frames saved: {saved_count}')

if __name__ == '__main__':
    # Use the video URL
    url = '_____YOUTUBE____LINK__HERE________'
    download_video(url)
    process_video('video.mp4')
