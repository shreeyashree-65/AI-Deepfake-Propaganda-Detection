import cv2
import os

# Paths to datasets
input_folders = {
    "real": "../dataset/deepfake_videos/real/",
    "fake": "../dataset/deepfake_videos/fake/"
}
output_folder = "../dataset/deepfake_frames/"

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# Extract frames from videos
def extract_frames(video_path, save_folder, label):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save every 10th frame to reduce redundancy
        if frame_count % 10 == 0:
            frame_name = f"{label}_{os.path.basename(video_path).split('.')[0]}_frame{frame_count}.jpg"
            frame_path = os.path.join(save_folder, frame_name)
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()

# Process both real and fake videos
for label, folder in input_folders.items():
    save_path = os.path.join(output_folder, label)
    os.makedirs(save_path, exist_ok=True)

    for video_file in os.listdir(folder):
        video_path = os.path.join(folder, video_file)
        extract_frames(video_path, save_path, label)

print("✅ Frame extraction complete!")
