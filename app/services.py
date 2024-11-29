# Importando a biblioteca pytube para baixar o vídeo do YouTube
from pytube import YouTube
import ffmpeg
import os

def download_audio_from_video(url, output_path="static/audio"):
    """
    Baixa o áudio do vídeo a partir da URL e converte para formato mp3.

    :param url: URL do vídeo do YouTube
    :param output_path: Caminho para salvar o áudio extraído
    :return: Caminho completo do arquivo de áudio
    """
    # Cria a pasta de saída caso ela não exista
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Baixando o vídeo
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    audio_file = video_stream.download(output_path=output_path)

    # Definindo o caminho de saída para o arquivo mp3
    output_audio = os.path.join(output_path, f"{yt.title}.mp3")

    # Convertendo o arquivo para MP3 usando ffmpeg
    ffmpeg.input(audio_file).output(output_audio).run()

    # Remover o arquivo de áudio original após a conversão
    os.remove(audio_file)

    return output_audio