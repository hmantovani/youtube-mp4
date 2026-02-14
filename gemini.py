# https://www.youtube.com/watch?v=ya2TeFOqlio

import yt_dlp
import pyperclip
import os

def download_video(link):
    # 1. Identifica o diretório onde este arquivo .py está salvo
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Define o caminho da subpasta 'downloads'
    download_folder = os.path.join(base_path, 'downloads')

    # 3. Se a pasta não existir, ele a cria automaticamente
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        print(f"Pasta criada em: {download_folder}")

    # Configurações do yt-dlp para salvar no caminho específico
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_folder}/%(title)s.%(ext)s', # Define o destino e nome
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando download em: {download_folder}")
            ydl.download([link])
        print("\nDownload concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")

def main():
    print("Verificando link no clipboard...")
    video_link = pyperclip.paste().strip()

    if "youtube.com" in video_link or "youtu.be" in video_link:
        download_video(video_link)
    else:
        print(f"Nenhum link do YouTube encontrado no clipboard. Conteúdo atual: {video_link}")

if __name__ == "__main__":
    main()