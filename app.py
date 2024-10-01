import yt_dlp
import os

# Função para baixar o vídeo em formato mp3
def download_youtube_video_as_mp3(url, output_path="."):
    ydl_opts = {
        'format': 'bestaudio/best',  # Baixa o melhor formato de áudio disponível
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Converte o áudio para mp3
            'preferredquality': '192',  # Qualidade do áudio em kbps
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Salva com o título do vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Erro ao baixar o serviço: {e}")
            pass

# Exemplo de uso
if __name__ == "__main__":

    urls = [
        "https://www.youtube.com/watch?v=3dK2B0o-Vxo&list=PLwUcLHw8fMWKUAeVtZjU1_13PcySGWPYB"
        #,""

    ]

    for i in urls:
        video_url = i#input("Digite a URL do vídeo do YouTube: ")
        output_directory = ""#input("Digite o diretório de saída (deixe em branco para salvar na pasta atual): ")

        if output_directory == "":
            output_directory = "."
    
        download_youtube_video_as_mp3(video_url, output_directory)
        print(f"Download concluído! O arquivo foi salvo em {output_directory}.\n")
