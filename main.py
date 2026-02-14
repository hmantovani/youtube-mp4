import customtkinter as ctk
import yt_dlp
import os
import pyperclip
from tkinter import filedialog, messagebox
from PIL import Image

class YoutubeDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Multi-Downloader")
        self.geometry("650x600")
        
        # Estado do idioma: True para Inglês, False para Português
        self.is_english = True
        
        # Dicionário de Traduções
        self.translations = {
            "en": {
                "title": "YouTube Downloader",
                "inst": "Paste links below (one per line) or import CSV/TXT files\n\nVideos save to 'downloads' folder",
                "btn_csv": "Import CSV",
                "btn_txt": "Import TXT",
                "btn_paste": "Paste clipboard (CTRL + V)",
                "btn_main": "START DOWNLOADS",
                "status_wait": "Status: Waiting...",
                "status_done": "Success! {} video(s) downloaded.",
                "msg_empty": "No links detected!",
                "msg_finish": "Process finished!",
                "lang_btn": "Português"
            },
            "pt": {
                "title": "YouTube Downloader",
                "inst": "Cole os links abaixo (um por linha) ou importe arquivos CSV/TXT\n\nVídeos são salvos na pasta 'downloads'",
                "btn_csv": "Importar CSV",
                "btn_txt": "Importar TXT",
                "btn_paste": "Colar clipboard (CTRL + V)",
                "btn_main": "INICIAR DOWNLOADS",
                "status_wait": "Status: Aguardando...",
                "status_done": "Sucesso! {} vídeo(s) baixado(s).",
                "msg_empty": "Nenhum link detectado!",
                "msg_finish": "Processo finalizado!",
                "lang_btn": "English"
            }
        }

        # Carregar Imagens das Bandeiras
        asset_path = os.path.join(os.path.dirname(__file__), "assets")
        self.img_us = ctk.CTkImage(light_image=Image.open(os.path.join(asset_path, "us.png")), size=(20, 20))
        self.img_br = ctk.CTkImage(light_image=Image.open(os.path.join(asset_path, "br.png")), size=(20, 20))

        # --- Botão de Troca de Idioma (Topo Direito) ---
        self.lang_button = ctk.CTkButton(self, text="Português", image=self.img_br, compound="right", 
                                         width=100, command=self.toggle_language)
        self.lang_button.pack(pady=10, padx=20, anchor="ne")

        # --- Elementos da Interface ---
        self.main_label = ctk.CTkLabel(self, text="", font=("Roboto", 24, "bold"))
        self.main_label.pack(pady=10)

        self.inst_label = ctk.CTkLabel(self, text="", font=("Roboto", 12), justify="left")
        self.inst_label.pack(pady=5)

        self.url_textbox = ctk.CTkTextbox(self, width=550, height=200)
        self.url_textbox.pack(pady=10)

        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.pack(pady=10)

        self.btn_csv = ctk.CTkButton(self.file_frame, text="", command=lambda: self.import_file("csv"))
        self.btn_csv.grid(row=0, column=0, padx=10)

        self.btn_txt = ctk.CTkButton(self.file_frame, text="", command=lambda: self.import_file("txt"))
        self.btn_txt.grid(row=0, column=1, padx=10)

        self.btn_paste = ctk.CTkButton(self.file_frame, text="", fg_color="gray", command=self.paste_from_clipboard)
        self.btn_paste.grid(row=0, column=2, padx=10)

        self.download_btn = ctk.CTkButton(self, text="", fg_color="#2b8a3e", font=("Roboto", 16, "bold"), 
                                          height=45, command=self.start_download_process)
        self.download_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.pack(pady=5)

        # Inicia com o idioma padrão
        self.update_ui_text()

    def toggle_language(self):
        self.is_english = not self.is_english
        self.update_ui_text()

    def update_ui_text(self):
        lang = "en" if self.is_english else "pt"
        data = self.translations[lang]

        # Atualiza todos os textos
        self.main_label.configure(text=data["title"])
        self.inst_label.configure(text=data["inst"])
        self.btn_csv.configure(text=data["btn_csv"])
        self.btn_txt.configure(text=data["btn_txt"])
        self.btn_paste.configure(text=data["btn_paste"])
        self.download_btn.configure(text=data["btn_main"])
        self.status_label.configure(text=data["status_wait"])
        
        # Atualiza o botão de idioma (mostra a bandeira do "próximo" idioma)
        if self.is_english:
            self.lang_button.configure(text="Português", image=self.img_br)
        else:
            self.lang_button.configure(text="English", image=self.img_us)

    def paste_from_clipboard(self):
        self.url_textbox.insert("end", pyperclip.paste() + "\n")

    def import_file(self, extension):
        file_path = filedialog.askopenfilename(filetypes=[(f"{extension.upper()} files", f"*.{extension}")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.url_textbox.insert("end", f.read() + "\n")

    def start_download_process(self):
        lang = "en" if self.is_english else "pt"
        raw_text = self.url_textbox.get("1.0", "end-1c")
        links = [line.strip() for line in raw_text.split('\n') if line.strip()]

        if not links:
            messagebox.showwarning("Aviso/Warning", self.translations[lang]["msg_empty"])
            return

        base_path = os.path.dirname(os.path.abspath(__file__))
        download_folder = os.path.join(base_path, 'downloads')
        if not os.path.exists(download_folder): os.makedirs(download_folder)

        self.download_btn.configure(state="disabled")
        
        count = 0
        for link in links:
            if "youtube.com" in link or "youtu.be" in link:
                self.status_label.configure(text=f"Download: {link[:30]}...", text_color="yellow")
                self.update_idletasks()
                if self.run_download(link, download_folder): count += 1

        self.status_label.configure(text=self.translations[lang]["status_done"].format(count), text_color="#2b8a3e")
        self.download_btn.configure(state="normal")
        messagebox.showinfo(self.translations[lang]["msg_finish"], f"Folder: {download_folder}")

    def run_download(self, link, folder):
        ydl_opts = {'format': 'best', 'outtmpl': f'{folder}/%(title)s.%(ext)s', 'quiet': True}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            return True
        except:
            return False

if __name__ == "__main__":
    app = YoutubeDownloaderApp()
    app.mainloop()