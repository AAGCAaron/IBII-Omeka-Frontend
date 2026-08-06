import re

file_path = 'd:/OMEKAS/src/PAPIIT/coleccionesPAPIIT/productosDeDifusionYDivulgacion.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="row g-4">', '<div class="row g-4 justify-content-center">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
