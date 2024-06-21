from .config import conn, cursor

import models.config

class Album:

    def __init__(self, id, title, year_released, number_of_songs, duration):
        self.id = id
        self.title = title
        self.year_released = year_released
        self.number_of_songs = number_of_songs
        self.duration = duration

    def __repr__(self):
        return f"<Album {self.title} {self.year_released} {self.number_of_songs} {self.duration}>"

    @classmethod
    def create_table(cls):
        #Shows the table of albums
        sql = """
            CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year_released TEXT NOT NULL,
            number_of_songs TEXT,
            duration INTEGER
            )
        """
        models.config.cursor.execute(sql)
        models.config.conn.commit()

    @classmethod
    def drop_table(cls):
        #Shows the table of albums
        sql = "DROP TABLE IF EXISTS albums;"
        models.config.cursor.execute(sql)
        models.config.conn.commit()

    def save(self):
        sql = """
            INSERT INTO albums (title, year_released, number_of_songs, duration)
            VALUES (?, ?, ?, ?)
        """
        models.config.cursor.execute(sql, (self.title, self.year_released, self.number_of_songs, self.duration))
        models.config.conn.commit()
        self.id = models.config.cursor.lastrowid

    @classmethod
    def create(cls, title, year_released, number_of_songs, duration):
        sql = """
            INSERT INTO albums (title, year_released, number_of_songs, duration)
            VALUES (?, ?, ?, ?)
        """
        models.config.cursor.execute(sql, (title, year_released, number_of_songs, duration))
        models.config.conn.commit()
        album = cls(models.config.cursor.lastrowid, title, year_released, number_of_songs, duration)
        return album

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM albums WHERE id = ?"
        models.config.cursor.execute(sql, (id,))
        row = models.config.cursor.fetchone()
        return cls(*row) if row else None

    def update(self):
        #Used to edit the details of an album
        sql = """
            UPDATE albums
            SET title = ?, year_released = ?, number_of_songs = ?, duration = ?
            WHERE id = ?
        """
        models.config.cursor.execute(sql, (self.title, self.year_released, self.number_of_songs, self.duration, self.id))
        models.config.conn.commit()

    def delete(self):
        #Deletes an album from the table
        sql = "DELETE FROM albums WHERE id = ?"
        models.config.cursor.execute(sql, (self.id,))
        models.config.conn.commit()
