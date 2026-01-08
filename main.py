import re, base64, sys, os
from dotenv import load_dotenv

load_dotenv()

def resource_path(relative_path):
    """Obtiene la ruta absoluta a un recurso, funciona tanto en desarrollo como empaquetado"""
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


vault_path = os.getenv("OBSIDIAN_VAULT")


""" markdowns= []

for item in OHB_path.iterdir():
    if item.is_file():
        markdowns.append(item) """


def md_to_latex_conversion(path: str, name: str):
    with open(path,'r', encoding='utf-8') as f:
        content = f.read()
    text = change_quotes(content)
    text = change_bold(text)
    text = change_italic(text)

    save = name + ".txt"

    with open(save,'w',encoding='utf-8') as f:
        f.write(text)

def latex_to_md_conversion(path: str, name: str):
    with open(path,'r', encoding='utf-8') as f:
        content = f.read()
    text = change_latex_bold(content)
    text = change_latex_quotes(text)
    text = change_latex_italic(text)

    save = name + '.md'

    with open(save,'w',encoding='utf-8') as f:
        f.write(text)


def change_bold(text):
    proc = re.sub(r'(?<!\*)\*\*([^*]+?)\*\*(?!\*)', r'\\textbf{\1}', text)
    return proc 

def change_italic(text):
    proc = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'\\textit{\1}', text)
    return proc 

def change_quotes(text):
    proc = re.sub(r'(^|(?<=\s))"', r'\\say{', text)
    aux = re.sub(r'(?<=¿)"', r'\\say{', proc)
    last = re.sub(r'"', r'}', aux )
    return last

def encoded_image_icon(file_img):
    with open(file_img, 'rb') as f:
        return base64.b64encode(f.read())
    
def change_latex_italic(text):
    proc = re.sub(r'\\textit{([^}]+)}', r'*\1*', text)
    return proc

def change_latex_bold(text):
    proc = re.sub(r'\\textbf{([^}]+)}', r'**\1**', text)
    return proc

def change_latex_quotes(text):
    proc = re.sub(r'\\say{([^}]+)}', r'"\1"', text)
    return proc

