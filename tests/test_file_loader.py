import pytest
from gerador_curriculo.utils.file_loader import load_json

def test_load_json():
    data = load_json('data/contact.json')
    assert isinstance(data, dict)
