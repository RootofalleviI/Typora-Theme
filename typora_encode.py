import os
from pathlib import Path

color_map = {
    'definition': '#52BE80', # green
    'theorem': '#A569BD', # purple
    'proposition': '#5499C7' , # blue
    'corollary': '#5499C7', # blue
    'lemma': '#F5B7B1', # pink
    'claim': '#F5B7B1', # pink
    'remark': 'dimgray', # dark gray
    'warning': '#C0392B', # dark red
    'caveat': '#C0392B', # dark red
    'example': '#F1C40F' # dark yellow
}

bgcolor_map = {
    'definition': '#EAFAF1', # green
    'theorem': '#F4ECF7', # purple
    'proposition': '#EBF5FB' , # blue
    'corollary': '#EBF5FB', # blue
    'lemma': '#FDEDEC', # pink
    'claim': '#FDEDEC', # pink
    'remark': '#F4F6F6', # dark gray
    'warning': '#F9EBEA', # dark red
    'caveat': '#F9EBEA', # dark red
    'example': '#FEF9E7', # dark yellow
}


start_token_map = {
    '**Definition': 'definition',
    '**Theorem': 'theorem',
    '**Proposition': 'proposition',
    '**Corollary': 'corollary',
    '**Lemma': 'lemma',
    '**Claim': 'claim',
    '**Remark': 'remark',
    '**Warning': 'warning',
    '**Caveat': 'caveat',
    '**Example': 'example'
}

def gen_str(content, color, bgcolor):
    _color = f'color: {color};'
    border_left = f'border-left: 5px solid {color};'
    background_color = f'background-color: {bgcolor};'
    margin = f'margin: 0 0 0 -25px;'
    padding = f'padding: 0 0 0 20px;'
    return f"<span style='{_color}{border_left}{background_color}{margin}{padding}'>{content} **</span>  "

def main(path):
    markdown_file = Path(path)
    if not markdown_file.exists():
        raise Exception(f"File DNE: {path}")

    with open(path) as f:
        lines = f.readlines()

    for idx in range(0, len(lines)):
        splitted = lines[idx].split('**  ', 1)
        for start_token in start_token_map:
            if splitted[0].startswith(start_token):
                splitted[0] = gen_str(splitted[0],
                    color_map[start_token_map[start_token]],
                    bgcolor_map[start_token_map[start_token]])
                lines[idx] = ''.join(splitted)


    with open(path, 'w') as f_new:
        for line in lines:
            f_new.write(line)

path = input()
main(path)
