import time
from pytube import YouTube
import os


def byemsg():
    bye = "Closing program, see you later."
    for letters in bye:
        time.sleep(0.1)
        print(letters, end='', flush=True)


def downloadvideo(directory):
    link = input("Link: ")
    path = directory
    print('Loading video info...')
    yt = YouTube(link)

    # Informações do vídeo
    print("Name: ", yt.title)
    print("Views: ", yt.views)
    print("Time: ", yt.length, "seconds")
    print("Rating: ", yt.rating)

    deci = (input("Are you sure to start the download? (Y/N) "))
    if deci not in 'yY':
        return

    # Instancia a uma variavél a maior resolução do vídeo
    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    # Baixa o vídeo no diretório digitado
    ys.download(path)
    print("Download finish.")


# Cria a pasta
def generatingdir(directory):
    if not os.path.isdir(directory):
        try:
            os.mkdir(directory)
        except OSError:
            print(f'Creation of the directory {directory} failed')
        else:
            print(f'Directory {directory} generated.')


if __name__ == '__main__':
    # Salva o diretorio atual
    cwd = os.getcwd()
    cwd += '\\Downloads'
    generatingdir(cwd)
    while True:
        downloadvideo(cwd)
        decision = (input("Want to download another video? (Y/N) "))
        if decision not in 'yY':
            break

    byemsg()
# IMPLEMENTAR INTERFACE GRÁFICA
