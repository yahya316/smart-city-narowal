from PIL import Image
import os

out_dir = r"d:\Vixonics\smart-city\assets\images"
src = os.path.join(out_dir, "logo.png")

img = Image.open(src).convert("RGBA")
pixels = img.load()
w, h = img.size

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if a < 20:
            continue
        # Near-white / silver outlined text -> charcoal black
        brightness = (r + g + b) / 3
        # Gold tones: high R/G, lower B, and not near-white
        is_goldish = r > 140 and g > 100 and b < 180 and (r - b) > 40 and brightness < 245
        is_near_white = brightness > 185 and abs(r - g) < 35 and abs(g - b) < 35 and abs(r - b) < 35
        if is_near_white and not is_goldish:
            # Keep some soft edge by blending with original alpha
            pixels[x, y] = (28, 28, 28, a)

out_path = os.path.join(out_dir, "logo-light.png")
img.save(out_path, "PNG", optimize=True)
print(f"Saved {out_path} ({img.size[0]}x{img.size[1]}, {os.path.getsize(out_path)} bytes)")

# Navbar-sized light logo
nav_h = 64
ratio = nav_h / img.height
nav = img.resize((int(img.width * ratio), nav_h), Image.Resampling.LANCZOS)
nav_path = os.path.join(out_dir, "logo-nav.png")
nav.save(nav_path, "PNG", optimize=True)
print(f"Nav logo: {nav.size}, {os.path.getsize(nav_path)} bytes")
