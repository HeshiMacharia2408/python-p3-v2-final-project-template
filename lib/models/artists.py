from .config import conn, cursor

import models.config
import ipdb

class Artist:

    def __init__(self, id, name, genre, album_id, albums):
        self.id = id
        self.name = name
        self.genre = genre
        self.album_id = album_id
        self.albums = albums

    def __repr__(self):
        return f"<Artist {self.name} {self.genre} {self.album_id} {self.albums}>"

    @classmethod
    #creates a table of artists
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            genre TEXT NOT NULL,
            album_id TEXT,
            albums INTEGER
            )
        """
        models.config.cursor.execute(sql)
        models.config.conn.commit()

    @classmethod
    def drop_table(cls):
        #Shows the table of artists
        sql = "DROP TABLE IF EXISTS artists;"
        models.config.cursor.execute(sql)
        models.config.conn.commit()

    # def save(self):
    #     sql = """
    #         INSERT INTO artists (name, genre, album_id, albums)
    #         VALUES (?, ?, ?, ?)
    #     """
    #     models.config.cursor.execute(sql, (self.name, self.genre, self.album_id, self.albums))
    #     models.config.conn.commit()
    #     self.id = models.config.cursor.lastrowid

    @classmethod
    def create(cls, name, genre, album_id, albums):
        sql = """
            INSERT INTO artists (name, genre, album_id, albums)
            VALUES (?, ?, ?, ?)
        """
        models.config.cursor.execute(sql, (name, genre, album_id, albums))
        models.config.conn.commit()

        artist = cls(models.config.cursor.lastrowid, name, genre, album_id, albums)
        return artist

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM artists WHERE id = ?"
        models.config.cursor.execute(sql, (id,))
        row = models.config.cursor.fetchone()
        return cls(*row) if row else None

    def update(self):
        #Used to edit the details of an artist
        sql = """
            UPDATE artists
            SET name = ?, genre = ?, album_id = ?, albums = ?
            WHERE id = ?
        """
        models.config.cursor.execute(sql, (self.name, self.genre, self.album_id, self.albums, self.id))
        models.config.conn.commit()

    @classmethod
    #Removes an artist from the table
    def delete(self, id):
        sql = "DELETE FROM artists WHERE id = ?"
        models.config.cursor.execute(sql, (id,))
        models.config.conn.commit()

    @classmethod
    def get_albums_for_artist(cls, artist_id):
        sql = "SELECT * FROM albums WHERE artist_id = ?"
        models.config.cursor.execute(sql, (artist_id,))
        rows = models.config.cursor.fetchall()
        albums = [albums(*row) for row in rows]
        return albums