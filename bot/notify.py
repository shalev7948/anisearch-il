import sqlite3
from bot.discord_bot import send

def run():
    conn = sqlite3.connect("anime.db")
    c = conn.cursor()

    rows = c.execute("""
        SELECT e.id, a.title, e.episode, s.url, a.image
        FROM episodes e
        JOIN anime a ON e.anime_id = a.id
        JOIN sources s ON s.episode_id = e.id
    """).fetchall()

    for r in rows:
        exists = c.execute("SELECT 1 FROM notified WHERE episode_id=?", (r[0],)).fetchone()

        if not exists:
            send(r[1], r[2], r[3], r[4])

            c.execute("INSERT INTO notified VALUES(?)", (r[0],))
            conn.commit()

    conn.close()
