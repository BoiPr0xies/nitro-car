#!/usr/bin/env python3
"""Build the interactive SVG entry from this project's UTF-8 HTML entry."""
from base64 import b64encode
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_bytes()
html.decode('utf-8', errors='strict')
payload = b64encode(html).decode('ascii')
svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
  <title>Nitro Car</title>
  <foreignObject width="100%" height="100%">
    <body xmlns="http://www.w3.org/1999/xhtml" style="margin:0;width:100%;height:100%">
      <iframe id="site" title="Nitro Car site" allow="autoplay; fullscreen; gamepad; clipboard-write" allowfullscreen="allowfullscreen" style="position:fixed;inset:0;width:100%;height:100%;border:0"></iframe>
      <script><![CDATA[
const bytes = Uint8Array.from(atob("''' + payload + '''"), ch => ch.charCodeAt(0));
document.getElementById("site").srcdoc = new TextDecoder("utf-8", {fatal:true}).decode(bytes);
      ]]></script>
    </body>
  </foreignObject>
</svg>
'''
(root / 'index.svg').write_text(svg, encoding='utf-8', newline='\n')
print('Built index.svg from index.html')
