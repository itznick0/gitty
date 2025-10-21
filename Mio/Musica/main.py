import os
import random
import time
import threading
from pathlib import Path

# ▼▼▼ CODICE playsound MINIMALE (solo per Windows) ▼▼▼
import ctypes
from ctypes import wintypes

winmm = ctypes.WinDLL('winmm')

def play_mp3(file_path):
    alias = "song_" + str(random.randint(1000, 9999))
    cmd = f'open "{file_path}" type mpegvideo alias {alias}'
    if winmm.mciSendStringW(cmd, None, 0, None) != 0:
        print(f"❌ Errore aprendo: {file_path}")
        return False

    cmd = f'play {alias} wait'
    winmm.mciSendStringW(cmd, None, 0, None)

    cmd = f'close {alias}'
    winmm.mciSendStringW(cmd, None, 0, None)
    return True
# ▲▲▲ FINE playsound ▲▲▲


class MusicPlayer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.playlist = []
        self.current_song = None
        self.stopped = False
        self.load_songs()

    def load_songs(self):
        """Carica tutti i file audio comuni dalla cartella"""
        # Estensioni supportate
        audio_extensions = {'.mp3', '.wav', '.ogg', '.flac', '.m4a', '.wma'}
        
        # Trova tutti i file con estensioni audio
        all_files = list(self.folder_path.iterdir())
        self.playlist = [
            f for f in all_files
            if f.is_file() and f.suffix.lower() in audio_extensions
        ]

        # Se non trova file audio, mostra un report dettagliato
        if not self.playlist:
            print(f"❌ Nessun file audio trovato in: {self.folder_path}")
            print("\n📁 File presenti nella cartella:")
            for f in all_files[:10]:  # Mostra solo i primi 10
                print(f"   - {f.name} (estensione: '{f.suffix}')")
            if len(all_files) > 10:
                print(f"   ... e altri {len(all_files) - 10} file")
            exit()

        print(f"✅ Trovati {len(self.playlist)} file audio:")
        for song in self.playlist[:5]:  # Mostra i primi 5
            print(f"   ▶️ {song.name}")
        if len(self.playlist) > 5:
            print(f"   ... e altri {len(self.playlist) - 5} brani")

        self.shuffle_playlist()

    def shuffle_playlist(self):
        random.shuffle(self.playlist)
        print("🔀 Playlist mescolata.")

    def play_next(self):
        if not self.playlist:
            print("🔁 Playlist finita. Ricomincio...")
            self.load_songs()

        self.current_song = self.playlist.pop(0)
        print(f"\n🎵 Ora in riproduzione: {self.current_song.name}")

        self.play_thread = threading.Thread(target=self._play_current)
        self.play_thread.start()

    def _play_current(self):
        play_mp3(str(self.current_song))
        if not self.stopped:
            self.play_next()

    def skip(self):
        print("⏭️ Saltata")
        winmm.mciSendStringW("stop all", None, 0, None)
        winmm.mciSendStringW("close all", None, 0, None)
        time.sleep(0.1)
        self.play_next()

    def stop(self):
        print("⏹️ Stop")
        winmm.mciSendStringW("stop all", None, 0, None)
        winmm.mciSendStringW("close all", None, 0, None)
        self.stopped = True

    def run(self):
        self.play_next()
        while not self.stopped:
            time.sleep(0.5)


def user_input_handler(player):
    print("\n🎛️  COMANDI:")
    print("  [S] → Salta canzone")
    print("  [Q] → Esci")
    print("  (Pausa non disponibile in questa versione)")

    while not player.stopped:
        cmd = input().strip().lower()
        if cmd == 's':
            player.skip()
        elif cmd == 'q':
            player.stop()
        else:
            print("❓ Usa S o Q")


if __name__ == "__main__":
    print("🎧 Benvenuto nel lettore musicale casuale!")
    print("Folder musica:     C:\ Users\ admin\ Desktop\ Informatica 2025\ Mio\ Musica      ")
    #folder = input("📁 Inserisci il percorso della cartella con la musica: ").strip()
    folder = "c:/Users/admin/Desktop/Informatica 2025/Mio/Musica"
    if not os.path.exists(folder):
        print("❌ Cartella non trovata!")
        exit()

    player = MusicPlayer(folder)

    input_thread = threading.Thread(target=user_input_handler, args=(player,))
    input_thread.daemon = True
    input_thread.start()

    try:
        player.run()
    except KeyboardInterrupt:
        player.stop()

    print("👋 A presto!")