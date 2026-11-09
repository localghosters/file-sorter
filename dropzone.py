
import os
import shutil
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"

CATEGORIES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".c", ".html", ".css", ".js", ".json"],
    "Installers": [".exe", ".msi"],
}

def organize():
    for file in DOWNLOADS.iterdir():
        if not file.is_file():
            continue

        category = "Other"

        for name, extensions in CATEGORIES.items():
            if file.suffix.lower() in extensions:
                category = name
                break

        folder = DOWNLOADS / category
        folder.mkdir(exist_ok=True)

        destination = folder / file.name

        # Prevent overwriting existing files
        counter = 1
        while destination.exists():
            destination = folder / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

        shutil.move(str(file), str(destination))
        print(f"[{category}] {file.name}")

    print("\nDownloads organized!")

if __name__ == "__main__":
    print("DropZone - Downloads Organizer")
    print("-" * 30)

    organize()
