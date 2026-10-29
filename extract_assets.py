#!/usr/bin/env python3
"""Post-process built pages: extract shared <style> and inline <script>
into styles.css / app.js so the deploy payload stays small."""
import re, pathlib

SRC = pathlib.Path('/home/hatch/workspace/your_files/blastertv-new-design')
PAGES = ['index.html','packages.html','features.html','channels.html','blog.html','faq.html']

style_text = None
script_text = None

for fname in PAGES:
    p = SRC / fname
    html = p.read_text()

    # extract <style> once (identical across pages)
    m = re.search(r'<style>(.*?)</style>', html, re.S)
    assert m, f'no style in {fname}'
    if style_text is None:
        style_text = m.group(1).strip()
    html = html.replace(m.group(0), '<link rel="stylesheet" href="styles.css">', 1)

    # extract the big inline script (the one without src=), keep CDN + insights tags
    scripts = list(re.finditer(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.S))
    assert scripts, f'no inline script in {fname}'
    big = max(scripts, key=lambda s: len(s.group(1)))
    if script_text is None:
        script_text = big.group(1).strip()
    html = html.replace(big.group(0), '<script src="app.js"></script>', 1)

    p.write_text(html)
    print('processed', fname, len(html), 'bytes')

(SRC / 'styles.css').write_text(style_text + '\n')
(SRC / 'app.js').write_text(script_text + '\n')
print('styles.css', len(style_text), 'bytes | app.js', len(script_text), 'bytes')
