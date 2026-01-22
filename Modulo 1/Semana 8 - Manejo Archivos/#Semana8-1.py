def read_document(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(f"Song: {line}")



def alfabetic_document(path):
    with open(path, "r", encoding="utf-8") as file:
        songs = file.readlines()
    songs_alfabetic = sorted(songs, key=str.lower)
    with open("songs_alfabetic.txt", "w", encoding="utf-8") as file:
        file.writelines(songs_alfabetic)


read_document('canciones.txt')
alfabetic_document('canciones.txt')
read_document('songs_alfabetic.txt')
