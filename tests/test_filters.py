from gerador_curriculo.utils.filters import filter_experiences

def test_filter_experiences():
    experiences = [
        {"title": "Dev Backend", "tags": ["backend", "python"]},
        {"title": "Dev Frontend", "tags": ["frontend", "javascript"]},
    ]
    tags = ["backend"]
    filtered = filter_experiences(experiences, tags)
    assert len(filtered) == 1
    assert filtered[0]["title"] == "Dev Backend"
