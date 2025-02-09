import os
import json

def load_json(file_path):
    """Carrega a fonte de dados a partir de um caminho para um arquivo json"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)