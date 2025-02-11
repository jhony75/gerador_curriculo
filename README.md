# Gerador de Currículo Automatizado

![GitHub License](https://img.shields.io/github/license/jhony75/gerador_curriculo)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/jhony75/gerador_curriculo)


---

Este projeto tem o intuito de facilitar a criação e manutenção de currículos para que sejam enviados para as mais diversas vagas, sempre mantendo a experiência relevante para a vaga em um template limpo, de fácil leitura que é compatível com sistemas de .

## Autores

- [jhony75](https://www.github.com/jhony75)

## Como instalar e utilizar

1. Clone o repositório
2. Na pasta clonada, rode o comando:

   ```poetry install```

3. Após isso, para rodar o projeto, use o comando:

   ```poetry run gerador-curriculo --tags lista de tags -l idioma```

--- 

Atualmente, os idiomas suportados para a template são:
- en -> Inglês
- pt -> Português (brasileiro)
--- 

As tags devem ser definidas no json "experiences", junto com a experiência relevante.  
Caso seja interessante para o usuário, a template conta com um '{}' vazio em alguns momentos, que pode ser utilizado para adicionar a localização.  
Os arquivos de contato e educação contam com as informações relevantes para as seções já organizadas de forma que possam ser utilizadas na template. As seções de "duties" e "skills" (tarefas e habilidades) ainda não foram implementadas e estão no roadmap para que o programa possa gerar um currículo resumido.  
Como mostrado no exemplo de como rodar o projeto, as tags devem ser passadas como texto plano, sem separadores nem aspas. 

## Próximos passos

- Separar o código em arquivos e funções mais adequados.
- Implementar as seções "duties" e "skills".
- Adequar o código a melhores práticas.
- Criar testes.
- Reorganizar a estrutura da pasta "data" e output"
- Criar e organizar comandos de forma que o script já gere o arquivo e rode o comando "pdflatex" direcionando para uma pasta apenas de pdfs, e oferecendo ao usuário a opção de deletar os outros arquivos gerados. 
- Avaliar a possibilidade de implementar outras templates ou adicionar mais informações as templates existentes.