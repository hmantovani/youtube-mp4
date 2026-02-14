# 📺 YouTube Multi-Downloader

<div align="center">
  <img src="assets/us.png" width="50" height="50"> 
  <img src="assets/uk.png" width="50" height="50">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/br.png" width="50" height="50"> 
  <img src="assets/pt.png" width="50" height="50">
</div>

---

## 🇺🇸 English Version

### 📝 Description
A modern desktop utility for downloading YouTube videos in high quality. This program supports single or bulk downloads, with features to import lists via text files, CSV spreadsheets, or by simply pasting multiple links from the clipboard.

### ✨ Features
* **Modern UI:** Clean and responsive look with Dark Mode support.
* **Bulk Download:** Paste dozens of links at once in the text area.
* **Flexible Import:** Dedicated buttons to load `.txt` or `.csv` files.
* **Auto-Management:** Automatically creates a `/downloads` folder within the script directory.

### 🚀 How to Run (Windows)
1. **Prerequisites:** Have **Python 3.x** installed and added to your PATH.
2. **Execution:**
   - Download or clone this repository.
   - Double-click the **`run.bat`** file.
   - The script will set up a virtual environment, install dependencies, and launch the app.

### 🛠️ Technologies
* **yt-dlp**: The download engine (always up to date).
* **CustomTkinter**: Modern Graphical User Interface.
* **Pyperclip**: Smart clipboard management.

---

## 🇧🇷 Versão em Português

### 📝 Descrição
Um utilitário de desktop moderno para baixar vídeos do YouTube em alta qualidade. Este programa permite downloads individuais ou em massa, com suporte para importação de listas via arquivos de texto, planilhas CSV ou simplesmente colando múltiplos links da área de transferência.

### ✨ Funcionalidades
* **Interface Moderna:** Visual limpo e responsivo com suporte a Dark Mode.
* **Download em Massa:** Cole dezenas de links de uma vez no campo de texto.
* **Importação Flexível:** Botões dedicados para carregar arquivos `.txt` ou `.csv`.
* **Auto-Gestão:** Cria automaticamente a pasta `/downloads` no diretório do script.

### 🚀 Como Rodar (Windows)
1. **Pré-requisitos:** Ter o **Python 3.x** instalado e adicionado ao PATH.
2. **Execução:**
   - Baixe ou clone este repositório.
   - Clique duas vezes no arquivo **`run.bat`**.
   - O script irá configurar o ambiente virtual, instalar as dependências e abrir o programa.

### 🛠️ Tecnologias
* **yt-dlp**: O motor de download (sempre atualizado).
* **CustomTkinter**: Interface gráfica moderna.
* **Pyperclip**: Gerenciamento inteligente da área de transferência.

---

## 📂 Project Structure / Estrutura do Projeto

```text
/youtube-mp4
├── main.py              # Main code / Código principal
├── requirements.txt     # Dependencies / Dependências
├── run.bat              # Startup script / Script de inicialização
├── assets/              # Icons and Flags / Ícones e Bandeiras
└── downloads/           # Saved videos / Vídeos salvos