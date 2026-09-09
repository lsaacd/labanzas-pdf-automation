import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'c:\Users\isaac\Downloads\Con Gozo Cantemos a Cristo Letra.pdf')
page = doc[0]
blocks = page.get_text('dict')['blocks']
for b in blocks:
    if 'lines' in b:
        for l in b['lines']:
            text = ''.join([s['text'] for s in l['spans']]).strip()
            if text:
                y = l['bbox'][1]
                x0 = l['bbox'][0]
                x1 = l['bbox'][2]
                mid = (x0 + x1) / 2
                font = l['spans'][0]['font']
                size = l['spans'][0]['size']
                print(f"y={y:5.1f} | x={x0:5.1f}..{x1:5.1f} (mid={mid:5.1f}) | font={font} {size:4.1f}pt | {text}")
