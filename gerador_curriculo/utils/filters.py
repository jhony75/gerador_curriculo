def filter_experiences(experiences, tags):
    """Filtra as experiências com base nas tags fornecidas"""
    return [
        exp for exp in experiences
        if any(tag in exp.get('tags', []) for tag in tags)
    ]