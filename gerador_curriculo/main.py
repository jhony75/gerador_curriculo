import argparse
import json
from jinja2 import Template
from gerador_curriculo.utils.file_loader import load_json
from gerador_curriculo.utils.filters import filter_experiences
from gerador_curriculo.utils.template_renderer import create_latex_environment

def main():
    # Configura os argumentos de CLI
    parser = argparse.ArgumentParser(description="Gerador de currículo Latex")
    parser.add_argument('-t', '--tags', nargs='+', required=True, help="Tags para filtrar experiências.")
    parser.add_argument('-l', '--lang', nargs='+', required=True, help="Idioma do currículo.")
    args = parser.parse_args()

    # Carregar dados
    contact = load_json('gerador_curriculo/data/contact.json')
    experiences = load_json('gerador_curriculo/data/experiences_en.json')
    education = load_json('gerador_curriculo/data/education_en.json')

    #tags = ["Salesforce","teaching"]
    #filtered_experiences = filter_experiences(experiences, tags)
    # Filtrar experiências
    filtered_experiences = filter_experiences(experiences, args.tags)
    print("Tags fornecidas: ", args.tags)
    print("Idioma: ", args.lang)

    # Combinar dados
    data = {
        "contact": {
            "name": contact["name"],
            "phone": contact["phone"],
            "email": contact["email"],
            "linkedin": contact["linkedin"],
            "skills": contact.get("skills", [])
        },
        "experiences": [
            {
                "title": exp["title"],
                "company": exp["company"],
                "duration": exp["duration"],
                "description": exp["description"]
            }
            for exp in filtered_experiences
        ],
        "education": [
            {
                "degree": edu["degree"],
                "institution": edu["institution"],
                "year": edu["year"],
            }
            for edu in education
        ]
    }

    #print(json.dumps(data, indent=4))

    # Cria o ambiente Jinja2
    env = create_latex_environment()

    # Carregar e renderizar o template
    with open('gerador_curriculo/templates/template_debug.tex.j2', 'r', encoding='utf-8') as f:
    #with open('gerador_curriculo/templates/template.tex.j2', 'r', encoding='utf-8') as f:
        template = env.from_string(f.read())

    lang = "pt"
    # Gerar o conteúdo com os dados
    output = template.render(data=data, lang=lang)

    # Salvar o resultado
    #with open('./output/curriculo.tex', 'w', encoding='utf-8') as f:
    with open('./output/resume_tests/resume_teste.tex', 'w', encoding='utf-8') as f:
        f.write(output)

    print("Currículo gerado com sucesso!")

if __name__ == '__main__':
    main()