import sqlite3

conn = sqlite3.connect('sqlite3/ps5.db')
c = conn.cursor()

games = [
    ("Grand Theft Auto : V (PS4)",
     "Grand Theft Auto V for PC offers players the option to explore the award-winning world of Los Santos and Blaine County in resolutions of up to 4k and beyond, as well as the chance to experience the game running at 60 frames per second.",
     199, "105.jpg", "old"),
    ("The Elder Scrolls V: Skyrim (PS3)",
     "The Elder Scrolls V: Skyrim is an action role-playing game, playable from either a first or third-person perspective. The player may freely roam over the land of Skyrim which is an open world environment consisting of wilderness expanses, dungeons, caves, cities, towns, fortresses, and villages.",
     199, "106.jpg", "old"),
    ("Need for Speed: Hot Pursuit (PS3)",
     "Need for Speed Hot Pursuit launches you into a new open-world landscape behind the wheel of the world's fastest and most beautiful cars. From Criterion, the award-winning studio behind the Burnout series, Hot Pursuit will redefine racing games for a whole new generation.",
     199, "107.jpg", "old"),
    ("Grand Theft Auto: Vice City (PS2)",
     "Welcome back to Vice City. Welcome back to the 1980s.From the decade of big hair, excess and pastel suits comes a story of one man's rise to the top of the criminal pile. Vice City, a huge urban sprawl ranging from the beach to the swamps and the glitz to the ghetto, was one of the most varied, complete and alive digital cities ever created.",
     199, "108.jpg", "old")
]
c.executemany('INSERT INTO games(name,desc,price,img_key,type) VALUES (?,?,?,?,?)', games)
conn.commit()
