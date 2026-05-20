## Calculadora de Média

## Integrantes:
Guilherme Bissi Fonseca
Arthur Santana
Samuel Bonfanti
Leonardo Moreno Pickler
Samuel Jorge
Lucas Prado

## Descrição

Sistema em Python que calcula a média aritmética de 4 notas e informa a situação do aluno.

## Como Executar

# 1. Clone o repositório
git clone https://github.com/aluno-fag/atividade-git-github-calculadora.git
cd atividade-git-github-calculadora

# 2. Execute o programa
python3 src/main.py

## Comandos Git Utilizados

```bash

# Iniciar repositório
git init -b main

# Criar repositório no GitHub (sem abrir o navegador)
gh repo create atividade-git-github-calculadora --private --source=. --remote=origin --push

# Ciclo do dia a dia
git status
git add .
git commit -m "mensagem descritiva"
git push

# Branches
git switch -c validacao
git push -u origin validacao
git switch master
git merge validacao
git push

# Histórico
git log --oneline
git log --oneline --graph --all

# Clonar em outra pasta (teste)
gh repo clone usuario/atividade-git-github-GASSLL teste-clone
```

---

## Histórico de Desenvolvimento
Primeiro commit — Criação dos arquivos e do repositório:
Criação do repositório com git init -b main e 
criação da estrutura de pastas do projeto.

Segundo commit — Desenvolvimento da calculadora

Desenvolvimento da calculadora em Python.
Calcula quatro notas informadas pelo usuário.
Informa a situação de acordo com as notas.

Terceiro commit — Elaboração dos requisitos funcionais
Elaboração dos requisitos funcionais do projeto.

Quarto commit — Adiciona .gitignore para o cache do Python

Criação do .gitignore.
Impedir que arquivos de cache do Python sejam enviados ao GitHub.

Quinto commit — Criação do README completo e diário de commits

Criação deste README.md com descrição, integrantes, como executar,
comandos Git utilizados e histórico de desenvolvimento. 
Criação do diario de commits com o registro detalhado de cada commit.


Commit 6 - Corrigir erros do projeto
Tratação de exceções utilizando ValueError.
Adicionando o main() no código.
Atualização de comandos da branch.

Commit 7 - Correção do clone do README.md  
Correção do comando clone que estava incorreto.