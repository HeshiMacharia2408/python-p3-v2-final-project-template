import models
import ipdb

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Artists")
        print("2. Manage Albums")
        print("3. Exit the App")
        choice = input("Select an Option: ")

        if choice == '1':
            artists_menu()
        elif choice == '2':
            albums_menu()
        elif choice == '3':
            exit('Exiting...')
        else:
            print('Please select a Valid Option.')

def artists_menu():
    while True:
        print("\nArtists Menu")
        print("1. Add Artist")
        print("2. Edit Artist")
        print("3. Delete Artist")
        print("4. Return to Main Menu")
        choice = input("Select an Option: ")

        if choice == '1':
            add_artist()
        elif choice == '2':
            edit_artist()
        elif choice == '3':
            delete_artist()
        elif choice == '4':
            break
        else:
            print("Please select a Valid Option.")

def add_artist():
    name = input("Enter artist name: ")
    genre = input("Enter artist genre: ")
    album_id = input("Enter album ID: ")
    albums = int(input("Enter number of albums: "))
    artist = models.Artist.create(name=name, genre=genre, album_id=album_id, albums=albums)
    print(f"Artist {name} added successfully.")

def edit_artist():
    id = int(input("Enter artist ID to edit: "))
    artist = models.Artist.find_by_id(id)
    if artist:
        artist.name = input(f"Enter new name (current: {artist.name}): ") or artist.name
        artist.genre = input(f"Enter new genre (current: {artist.genre}): ") or artist.genre
        artist.album_id = input(f"Enter new album ID (current: {artist.album_id}): ") or artist.album_id
        artist.albums = input(f"Enter new number of albums (current: {artist.albums}): ") or artist.albums
        artist.update()
        print(f"Artist {artist.name} updated successfully.")
    else:
        print(f"No artist found with the ID {id}.")

def delete_artist():
    id = int(input("Enter artist ID to delete: "))
    artist = models.Artist.find_by_id(id)
    if artist:
        models.Artist.delete(artist.id)
        print(f"Artist {id} deleted successfully.")
    else:
        print(f"No artist found with the ID {id}.")

def albums_menu():
    while True:
        print("\nAlbums Menu")
        print("1. Add Album")
        print("2. Edit Album")
        print("3. Delete Album")
        print("4. Return to Main Menu")
        choice = input("Select an Option: ")

        if choice == '1':
            add_album()
        elif choice == '2':
            edit_album()
        elif choice == '3':
            delete_album()
        elif choice == '4':
            break
        else:
            print("Please select a Valid Option.")

def add_album():
    title = input("Enter album title: ")
    year_released = input("Enter year released: ")
    number_of_songs = input("Enter number of songs: ")
    duration = int(input("Enter duration in minutes: "))
    album = models.Album.create(title=title, year_released=year_released, number_of_songs=number_of_songs, duration=duration)
    print(f"Album {title} added successfully.")

def edit_album():
    album_id = int(input("Enter album ID to edit: "))
    album = models.Album.find_by_id(album_id)
    if album:
        album.title = input(f"Enter new title (current: {album.title}): ") or album.title
        album.year_released = input(f"Enter new year released (current: {album.year_released}): ") or album.year_released
        album.number_of_songs = input(f"Enter new number of songs (current: {album.number_of_songs}): ") or album.number_of_songs
        album.duration = input(f"Enter new duration (current: {album.duration}): ") or album.duration
        album.update()
        print(f"Album {album.title} updated successfully.")
    else:
        print(f"No album found with the ID {album_id}.")

def delete_album():
    title = int(input("Enter album title to delete: "))
    album = models.Album.find_by_id(title)
    if album:
        album.delete()
        print(f"Album {album.title} deleted successfully.")
    else:
        print(f"No album found with the title {title}.")

if __name__ == "__main__":
    main_menu()
