from PIL import Image
import os

src = r"C:\Users\yahya\Downloads\smart city logo with text.png"
icon_src = r"D:\Vixonics\real-estate\smart city logo with no text.png"
out_dir = r"d:\Vixonics\smart-city\assets\images"


def remove_black_bg(path, out_path, threshold=40, max_w=900):
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r <= threshold and g <= threshold and b <= threshold:
                pixels[x, y] = (0, 0, 0, 0)
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.Resampling.LANCZOS)
    img.save(out_path, "PNG", optimize=True)
    print(f"Saved {out_path} ({img.size[0]}x{img.size[1]}, {os.path.getsize(out_path)} bytes)")
    return img


remove_black_bg(src, os.path.join(out_dir, "logo.png"), threshold=40, max_w=900)
remove_black_bg(icon_src, os.path.join(out_dir, "logo-icon.png"), threshold=40, max_w=400)

nav = Image.open(os.path.join(out_dir, "logo.png"))
nav_h = 72
ratio = nav_h / nav.height
nav = nav.resize((int(nav.width * ratio), nav_h), Image.Resampling.LANCZOS)
nav_path = os.path.join(out_dir, "logo-nav.png")
nav.save(nav_path, "PNG", optimize=True)
print(f"Nav logo: {nav.size}, {os.path.getsize(nav_path)} bytes")
