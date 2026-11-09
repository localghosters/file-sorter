# DropZone 📦

A lightweight Python utility that automatically organizes your Downloads folder into categorized directories.

## Features

- Automatically categorizes downloaded files.
- Supports images, videos, documents, archives, code, and installers.
- Moves uncategorized files into an `Other` folder.
- Prevents overwriting files with duplicate names.
- Creates category folders automatically.
- Zero external dependencies.

## Categories

| Category | Extensions |
|---|---|
| Images | PNG, JPG, JPEG, GIF, WEBP, SVG |
| Videos | MP4, MKV, MOV, AVI |
| Documents | PDF, DOCX, DOC, TXT, PPTX, XLSX |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, CPP, C, HTML, CSS, JS, JSON |
| Installers | EXE, MSI |
| Other | Everything else |

## Requirements

- Python 3.8+
- No external packages required

## Usage

```bash
git clone https://github.com/yourusername/dropzone.git
cd dropzone
python dropzone.py
```

DropZone automatically organizes files inside your Windows Downloads directory.

## Example

Before:

```text
Downloads/
├── photo.png
├── notes.pdf
├── app.exe
└── project.py
```

After:

```text
Downloads/
├── Images/
│   └── photo.png
├── Documents/
│   └── notes.pdf
├── Installers/
│   └── app.exe
└── Code/
    └── project.py
```

## Safety

DropZone moves files rather than copying them. Existing files are not overwritten; duplicate filenames receive numbered suffixes.

Review the source code before running it on important files.

## License

MIT License
