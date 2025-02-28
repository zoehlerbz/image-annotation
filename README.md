# Anotação automática de imagens para treinamento de modelo YOLO

Este projeto tem como objetivo automatizar a anotação de imagens no formato YOLO, facilitando a criação de datasets para modelos de detecção de objetos. Inicialmente pensado para a classe **"bird"**, o projeto pode ser adaptado para outros objetos compatíveis com o modelo YOLO.

A ferramenta utiliza o próprio YOLO para identificar o objeto de interesse em uma imagem, com base em um ponto de corte de probabilidade. Quando o objeto é detectado, um arquivo .txt é gerado automaticamente com as informações de anotação necessárias. O usuário apenas precisa fornecer uma tabela que relacione a classe desejada ao nome da imagem correspondente.

## ⚠️ OBSERVAÇÃO

A anotação de imagens é um processo essencial no treinamento de modelos de visão computacional, mas pode ser extremamente demorada, especialmente ao lidar com grandes bancos de imagens. **Este projeto não substitui a anotação manual**, mas serve como um suporte valioso para acelerar e otimizar o processo.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/image-annotation.git
```
2. Navegue até o diretório do projeto:

```bash
cd image-annotation
```
3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como usar

Prepare suas imagens de entrada (em formato .jpg) e coloque-as na pasta 'image_annotation/data/raw'. 

1. Execute o script:

```bash
python run.py
```
