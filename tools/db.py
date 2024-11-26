import sqlite3
import os

def init():
    
    db_file = 'game.db'

    
    if not os.path.exists(db_file):
        
        conn = sqlite3.connect(db_file)
        
       
        cursor = conn.cursor()
        
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rounds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                round DATETIME DEFAULT CURRENT_TIMESTAMP,
                player_what_he_played INTEGER,
                bot_what_he_played INTEGER,
                player_win BOOLEAN
            )
        ''')
        
        
        conn.commit()
        conn.close()

        print("Database and table created successfully.")
    else:
        print("Database already exists.")

def add_round(player_what_he_played, bot_what_he_played, player_win):
    
    db_file = 'game.db'
    
    
    conn = sqlite3.connect(db_file)
    
    
    cursor = conn.cursor()
    
    
    cursor.execute('''
        INSERT INTO rounds (player_what_he_played, bot_what_he_played, player_win)
        VALUES (?, ?, ?)
    ''', (player_what_he_played, bot_what_he_played, player_win))
    conn.commit()
    conn.close()
init()
