<h2 align="center"> 📷 Técnicas de Não Repúdio para Proteção contra Fake Nudes 📷</h2>

<p align="center">Projeto desenvolvido em Python durante a disciplina de Segurança em Sistemas de Computação - <a href="https://sites.google.com/a/ice.ufjf.br/edelbertofranco/disciplinas/gradua%C3%A7%C3%A3o/2024-1-dcc075-seguran%C3%A7a?authuser=0">DCC075</a>, ministrado pelo professor <a href="https://sites.google.com/a/ice.ufjf.br/edelbertofranco/">Edelberto Franco Silva</a>.</p>

<h4 align="center"> 
	👨🏾‍💻 Python 👩‍💻 </h4>

## 📌 Instalando as bibliotecas necessárias

```bash
# Pillow: Biblioteca de manipulação de imagens;
# Cryptography: Biblioteca para operações criptográficas, incluindo assinaturas digitais.
# NumPy: Biblioteca para operações eficientes em arrays e matrizes, útil para manipulação de pixels.
pip install Pillow cryptography numpy
```
## 💻 Rodando aplicação no Linux

Para rodar os testes de assinatura digital
```bash
python test_digital_signature.py
```
Para rodar os testes de integridade com hashing
```bash
python teste_de_integridade_hashing.py
```

Para rodar os teste com watermark
```bash
python test_watermark.py
```
Existe 3 opções:

	1 - Comparando as imagens originais com as imagens modificadas (Aqui, basta colocar as imagens originais na pasta img, e as modificadas na pasta img_modificado. OBS: é necessario que o nome das imagens originas e as imagens modificadas sejam o mesmo)

	2 - Comparando as imagens originais com as imagens originais(Aqui, basta colocar as imagens originais na pasta img, e as copias das não modificadas na pasta img_integra. OBS: é necessario que o nome das imagens originas e as imagens copias sejam o mesmo)

	3 - digitar pasta de origem e pasta de destino(Aqui, basta digitar o nome de duas pastas, uma contendo as originas, a outra as modificadas, de forma semelhante as outras opções, o nome das imagens devem ser o mesmo em ambas as pastas)


## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:
- [Git](https://git-scm.com/)
- [Python](https://python.org/)

## 👨‍💻 Autores
- Ágata Meireles Carvalho - [GitHub](https://github.com/agatameireles11)
- Kleiton Ewerton de Oliveira - [GitHub](https://github.com/KleitonEwerton)
- NiKolas Oliver Sales Genesio - [GitHub](https://github.com/nikolasgenesio)


## 📞 Contatos
- agata.meireles@gmail.com / agata.meireles@estudante.ufjf.br
- kleitonewertonoliveira@gmail.com  
- nikolasgenesio@gmail.com
