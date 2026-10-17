import os

folder = "assets/awb20260613"  # path to your photos, relative to your HTML file
exts = (".jpg", ".jpeg", ".png", ".webp")

files = sorted(f for f in os.listdir(folder) if f.lower().endswith(exts))

with open("gallery-snippet.html", "w", encoding="utf-8") as out:
    out.write('<div class="gallery">\n')
    for f in files:
        out.write(f'  <a href="{folder}/{f}"><img src="{folder}/{f}" alt="Arts Without Boundaries, 13 June 2026" loading="lazy"></a>\n')
    out.write('</div>\n')

print(len(files), "images written")
