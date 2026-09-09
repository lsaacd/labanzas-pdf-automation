import fitz
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
doc = fitz.open(r'c:\Users\isaac\Downloads\Con Gozo Cantemos a Cristo Letra.pdf')
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save('letra_sample.png')
print('Saved letra_sample.png')
print('Page rect:', page.rect)
print('Fonts:', page.get_fonts())

page_dict = page.get_text('dict')
for b in page_dict['blocks']:
    if 'lines' in b:
        for l in b['lines']:
            line_str = " ".join([s['text'] for s in l['spans']])
            font_info = ", ".join(set([f"{s['font']} {s['size']:.1f}pt" for s in l['spans']]))
            print(f"[{font_info}] @ ({l['bbox'][0]:.1f}, {l['bbox'][1]:.1f}): {line_str}")
