from pathlib import Path

dirs = {
    ".png": "Images",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".pfd": "Documents",
    ".mp3": "Musiques",
}

tri_dir = Path(r"C:\Tri")
print(tri_dir)
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    print(f.name)
    # ext = f.suffix.lower().lstrip('.')  # en minuscule, sans point
    # output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    # output_dir.mkdir(parents=True, exist_ok=True)
    # f.rename(output_dir / f.name)
