import os
from bs4 import BeautifulSoup

file_path = 'd:/OMEKAS/src/PAPIIT/coleccionesPAPIIT/productosDeDifusionYDivulgacion.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

col_12s = soup.select('.row.g-4 > .col-12')

for col_12 in col_12s:
    horizontal_card = col_12.find('div', class_='horizontal-card')
    if not horizontal_card:
        continue
    
    # Extract cover info
    cover_col = horizontal_card.find('div', class_='cover-column')
    cover_classes = cover_col.get('class', [])
    color_class = [c for c in cover_classes if c.startswith('cover-') and c != 'cover-column'][0]
    
    cover_content = cover_col.find('div', class_='cover-content')
    icon_tag = cover_content.find('i')
    if icon_tag and icon_tag.string == '\xa0':
        icon_tag.string = '\u200D' # zwj
    
    label_tag = cover_content.find('span')
    label_text = label_tag.text.strip()
    
    # Extract card body info
    card_body = horizontal_card.find('div', class_='card-body')
    title = card_body.find('h5')
    
    paras = card_body.find_all('p')
    subtitle = paras[0] if len(paras) > 0 else None
    desc = paras[1] if len(paras) > 1 else None
    if desc:
        desc['class'] = desc.get('class', []) + ['flex-grow-1']
        
    actions = card_body.find('div', class_=lambda c: c and 'justify-content-end' in c and not 'text-end' in c)
    if not actions:
        # Sometimes the actions is a text-end div
        actions = card_body.find('div', class_=lambda c: c and 'text-end' in c)
    
    # If actions has buttons, fix their icons
    if actions:
        for i_btn in actions.find_all('i'):
            if i_btn.string == '\xa0':
                i_btn.string = '\u200D'
        actions['class'] = 'mt-4 text-end'
        
    # Build new vertical card structure
    col_12['class'] = 'col-md-6 col-lg-4 d-flex align-items-stretch'
    
    new_card = soup.new_tag('div', **{'class': 'card shadow-sm border-0 rounded-4 overflow-hidden position-relative w-100'})
    
    new_top = soup.new_tag('div', **{'class': f'{color_class} d-flex flex-column align-items-center justify-content-center p-4 text-center', 'style': 'min-height: 160px; position: relative;'})
    if icon_tag:
        icon_tag['class'] = [c.replace('display-5', 'display-4') for c in icon_tag.get('class', [])]
        icon_tag['class'] = [c for c in icon_tag['class'] if c != 'mb-2'] + ['mb-2']
        new_top.append(icon_tag)
    
    if label_tag:
        label_tag['style'] = 'font-size: 0.75rem; letter-spacing: 1px; z-index: 2;'
        label_tag['class'] = [c for c in label_tag.get('class', []) if 'text-white' not in c] + ['text-white']
        new_top.append(label_tag)
        
    new_card.append(new_top)
    
    new_body = soup.new_tag('div', **{'class': 'card-body p-4 d-flex flex-column'})
    if title:
        new_body.append(title)
    if subtitle:
        new_body.append(subtitle)
    if desc:
        new_body.append(desc)
    if actions:
        new_body.append(actions)
        
    new_card.append(new_body)
    
    # Replace the old horizontal card with the new card
    horizontal_card.replace_with(new_card)

# Write output
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
