import os

folder = "assets/copskids20260817"  # path to your photos, relative to your HTML file
exts = (".jpg", ".jpeg", ".png", ".webp")

files = sorted(f for f in os.listdir(folder) if f.lower().endswith(exts))

with open("galleries/gallery-snippet.html", "w", encoding="utf-8") as out:
    out.write('<div class="gallery">\n')
    for i, f in enumerate(files, start=1):
        out.write(f'  <a href="{folder}/{f}"><img src="{folder}/{f}" alt="Cops vs. Kids Basketball game, 17 August 2026, photo {i} of {len(files)}" loading="lazy"></a>\n')
    out.write('</div>\n')

print(len(files), "images written")
