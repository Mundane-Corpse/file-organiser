import os
from datetime import datetime

folder = "test_folder"
os.makedirs(folder, exist_ok=True)
fake_file = ["photo.jpg", "resume.pdf", "selfie.jpg", "notes.pdf", "data.csv", "video.mp4"]
for file in fake_file:
    open(os.path.join(folder, file), "w").close()

categories = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".txt", ".docx"],
        "data": [".csv", ".xlsx"],
        "Videos": [".mp4", ".mov"]
    }

log = []
for file in os.listdir(folder):
        name,ext = os.path.splitext(file)

        for category, extensions in categories.items():
            if ext in extensions:
                dest = os.path.join(folder, category)
                os.makedirs(dest, exist_ok=True)
                os.rename(
                     os.path.join(folder, file),
                     os.path.join(dest, file)
                )
                message = f"Moved {file} to {category}"
                print(message)
                log.append(message)

log_filename = f"log_{datetime.now().strftime('%Y-%m-%d')}.txt"
with open(log_filename, "w") as f:
    for entry in log:
        f.write(entry + "\n")

print(f"\nLog saved to {log_filename}")