import sqlite3

conn = sqlite3.connect('sqlite3/ps5.db')
c = conn.cursor()

games = [
    ("Call Of Duty : Warzone",
     "Warzone is a new, massive combat experience with up to 150 players from the world of Call of Duty: Modern Warfare and is free-to-play for everyone.",
     599, "101.jpg", "new"),
    ("Fortnite",
     "Fortnite is a survival game where 100 players fight against each other in player versus player combat to be the last one standing. It is a fast-paced, action-packed game, not unlike The Hunger Games, where strategic thinking is a must in order to survive.",
     299, "102.jpg", "old"),
    ("Minecraft",
     "Explore infinite worlds and build everything from the simplest of homes to the grandest of castles. Play in creative mode with unlimited resources or mine deep into the world in survival mode, crafting weapons and armor to fend off dangerous mobs.",
     0, "103.jpg", "old"),
    ("PUBG",
     "PUBG delivers the most intense free-to-play multiplayer action on mobile. Drop in, gear up, and compete. Survive epic 100-player classic battles, payload mode and fast-paced 4v4 team deathmatch and zombie modes. ",
     999, "104.jpg", "old")
]
c.executemany('INSERT INTO games(name,desc,price,img_key,type) VALUES (?,?,?,?,?)', games)
conn.commit()
